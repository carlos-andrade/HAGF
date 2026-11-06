#!/usr/bin/env python3
"""
HAGF Public Recovery
Baixa SOMENTE URLs de arquivos explicitamente declaradas em config/fontes_publicas.json.

Não faz crawling, descoberta de links, scraping de páginas, login, bypass de paywall,
enumeração de endpoints ou coleta de dados pessoais.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, unquote
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "fontes_publicas.json"
OUT = ROOT / "dados" / "recovery"
REPORTS = ROOT / "research" / "execucoes"
USER_AGENT = "HAGF-Public-Document-Recovery/1.0 (explicit-URL downloads; no crawler)"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def safe_name(value: str) -> str:
    value = unquote(value or "").split("?")[0].split("#")[0]
    name = Path(value).name or "documento"
    name = re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("._")
    return name[:160] or "documento"


def load_config() -> dict:
    with CONFIG.open("r", encoding="utf-8") as f:
        cfg = json.load(f)
    if cfg.get("policy", {}).get("mode") != "explicit_direct_download_only":
        raise ValueError("Modo de coleta inesperado; execução bloqueada.")
    return cfg


def validate_url(url: str, allowed_hosts: list[str]) -> tuple[bool, str]:
    p = urlparse(url)
    if p.scheme != "https":
        return False, "BLOCKED_NON_HTTPS"
    if not p.hostname or p.hostname.lower() not in {h.lower() for h in allowed_hosts}:
        return False, "BLOCKED_HOST_NOT_ALLOWLISTED"
    if p.username or p.password:
        return False, "BLOCKED_CREDENTIALS_IN_URL"
    return True, "OK"


def download_one(source: dict, policy: dict, execute: bool) -> dict:
    url = source.get("download_url")
    base = {
        "source_id": source.get("id"),
        "source_reference": source.get("url"),
        "download_url": url,
        "checked_at_utc": utc_now(),
    }
    if not url:
        return {**base, "status": "SKIPPED_NO_DIRECT_DOWNLOAD_URL"}
    valid, reason = validate_url(url, policy["allowed_hosts"])
    if not valid:
        return {**base, "status": reason}
    if not execute:
        return {**base, "status": "VALIDATED_DRY_RUN"}
    max_bytes = int(policy.get("max_file_mb", 80)) * 1024 * 1024
    timeout = int(policy.get("request_timeout_seconds", 25))
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/pdf,application/octet-stream,*/*"})
    try:
        with urlopen(req, timeout=timeout) as response:
            final_url = response.geturl()
            ok, why = validate_url(final_url, policy["allowed_hosts"])
            if not ok:
                return {**base, "status": "BLOCKED_REDIRECT", "detail": why}
            content_type = response.headers.get("Content-Type", "").split(";")[0].lower()
            disposition = response.headers.get("Content-Disposition", "")
            raw_name = None
            match = re.search(r'filename\*?=(?:UTF-8\'\')?"?([^";]+)', disposition, re.I)
            if match:
                raw_name = match.group(1)
            name = safe_name(raw_name or urlparse(final_url).path)
            data = response.read(max_bytes + 1)
            if len(data) > max_bytes:
                return {**base, "status": "BLOCKED_SIZE_LIMIT", "content_type": content_type}
            if not data:
                return {**base, "status": "EMPTY_RESPONSE", "content_type": content_type}
            # Evita gravar páginas HTML por engano como se fossem documentos baixáveis.
            if "text/html" in content_type or data.lstrip()[:20].lower().startswith((b"<!doctype html", b"<html")):
                return {**base, "status": "BLOCKED_HTML_NOT_FILE", "content_type": content_type}
            if content_type not in ("application/pdf", "application/octet-stream", "application/zip",
                                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"):
                return {**base, "status": "REVIEW_UNEXPECTED_CONTENT_TYPE", "content_type": content_type}
            OUT.mkdir(parents=True, exist_ok=True)
            target = OUT / name
            if target.exists():
                digest = hashlib.sha256(data).hexdigest()
                if hashlib.sha256(target.read_bytes()).hexdigest() == digest:
                    return {**base, "status": "ALREADY_PRESENT_IDENTICAL", "file": str(target.relative_to(ROOT)),
                            "sha256": digest, "bytes": len(data), "content_type": content_type}
                target = OUT / f"{target.stem}_{digest[:10]}{target.suffix}"
            target.write_bytes(data)
            return {**base, "status": "DOWNLOADED", "file": str(target.relative_to(ROOT)),
                    "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
                    "content_type": content_type, "final_url": final_url}
    except HTTPError as e:
        return {**base, "status": "HTTP_ERROR", "http_status": e.code}
    except (URLError, TimeoutError, OSError) as e:
        return {**base, "status": "NETWORK_ERROR", "detail": str(e)[:400]}


def main() -> int:
    global CONFIG
    parser = argparse.ArgumentParser(description="Coleta controlada de arquivos públicos do HAGF.")
    parser.add_argument("--execute", action="store_true", help="Executa downloads de URLs diretas explícitas.")
    parser.add_argument("--config", type=Path, default=CONFIG)
    args = parser.parse_args()
    CONFIG = args.config
    cfg = load_config()
    policy = cfg["policy"]
    OUT.mkdir(parents=True, exist_ok=True)
    results = [download_one(s, policy, args.execute) for s in cfg.get("sources", [])]
    run = {
        "project": "HAGF",
        "started_at_utc": utc_now(),
        "mode": "EXECUTE" if args.execute else "DRY_RUN",
        "policy": policy,
        "source_count": len(results),
        "results": results,
        "summary": {},
    }
    for item in results:
        status = item["status"]
        run["summary"][status] = run["summary"].get(status, 0) + 1
    REPORTS.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report_path = REPORTS / f"HAGF_PUBLIC_RECOVERY_{stamp}.json"
    report_path.write_text(json.dumps(run, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"report": str(report_path.relative_to(ROOT)), "mode": run["mode"],
                      "source_count": run["source_count"], "summary": run["summary"]},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
