#!/usr/bin/env python3
"""HAGF Preservation Ledger: automated inventory, provenance and integrity checks.

This module does not request source URLs or crawl websites. It inventories the
manifest and local archive, and marks ingestion as blocked/pending when no
authorized automated adapter is configured.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "config" / "fontes_publicas.json"
DEFAULT_ARCHIVE = ROOT / "dados" / "recovery"
DEFAULT_REPORTS = ROOT / "research" / "execucoes"


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def classify_source(source: dict, archive_root: Path) -> dict:
    source_id = source.get("id", "UNKNOWN")
    direct_url = source.get("download_url")
    expected_path = source.get("archive_path")
    result = {
        "source_id": source_id,
        "source_type": source.get("type", ""),
        "source_url": source.get("url", ""),
        "download_url": direct_url or "",
        "archive_path": "",
        "bytes": 0,
        "sha256": "",
        "status": "",
        "capture_method": "NOT_CONFIGURED",
        "checked_at_utc": now_utc(),
        "notes": "",
    }

    if expected_path:
        candidate = (ROOT / expected_path).resolve()
        if ROOT.resolve() not in candidate.parents:
            result.update(status="BLOCKED_PATH_TRAVERSAL", notes="archive_path fora do repositório")
            return result
        if candidate.is_file():
            result.update(
                archive_path=str(candidate.relative_to(ROOT)),
                bytes=candidate.stat().st_size,
                sha256=sha256_file(candidate),
                status="PRESERVED",
                capture_method=source.get("capture_method", "LOCAL_ARCHIVE"),
            )
            return result

    if direct_url:
        result.update(
            status="RECOVERED_PRIOR_RUN_NOT_MATERIALIZED",
            capture_method="DIRECT_FILE_URL",
            notes="Existe URL direta; artefacto não está presente no workspace atual. Não presumir cópia local.",
        )
        return result

    result.update(
        status="AUTHORIZATION_REQUIRED",
        capture_method="NONE",
        notes="Referência HTML; ingestão automatizada depende de API/exportação oficial ou autorização específica.",
    )
    return result


def build_ledger(manifest: dict, archive_root: Path) -> dict:
    sources = manifest.get("sources", [])
    records = [classify_source(source, archive_root) for source in sources]
    summary: dict[str, int] = {}
    for record in records:
        summary[record["status"]] = summary.get(record["status"], 0) + 1
    return {
        "project": "HAGF",
        "schema_version": "1.0",
        "generated_at_utc": now_utc(),
        "source_count": len(records),
        "summary": summary,
        "records": records,
    }


def write_outputs(ledger: dict, reports_dir: Path) -> tuple[Path, Path]:
    reports_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    json_path = reports_dir / f"HAGF_PRESERVATION_LEDGER_{stamp}.json"
    csv_path = reports_dir / f"HAGF_PRESERVATION_LEDGER_{stamp}.csv"
    json_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = [
        "source_id", "source_type", "source_url", "download_url", "archive_path",
        "bytes", "sha256", "status", "capture_method", "checked_at_utc", "notes",
    ]
    with csv_path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(ledger["records"])
    return json_path, csv_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera inventário automatizado de preservação HAGF.")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--reports", type=Path, default=DEFAULT_REPORTS)
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    ledger = build_ledger(manifest, args.archive)
    json_path, csv_path = write_outputs(ledger, args.reports)
    print(json.dumps({
        "source_count": ledger["source_count"],
        "summary": ledger["summary"],
        "json_report": str(json_path.relative_to(ROOT)),
        "csv_report": str(csv_path.relative_to(ROOT)),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
