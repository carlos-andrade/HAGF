import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import hagf_preservation_ledger as ledger


class PreservationLedgerTests(unittest.TestCase):
    def test_html_reference_is_not_fetched_and_requires_authorized_adapter(self):
        record = ledger.classify_source(
            {"id": "HTML1", "type": "help_article_reference", "url": "https://ajuda.agf.com.br/article"},
            ROOT / "dados" / "recovery",
        )
        self.assertEqual(record["status"], "AUTHORIZATION_REQUIRED")
        self.assertEqual(record["capture_method"], "NONE")

    def test_direct_file_without_local_copy_is_not_marked_preserved(self):
        record = ledger.classify_source(
            {"id": "PDF1", "type": "legal_document", "url": "https://example.org/a", "download_url": "https://example.org/a.pdf"},
            ROOT / "dados" / "recovery",
        )
        self.assertEqual(record["status"], "RECOVERED_PRIOR_RUN_NOT_MATERIALIZED")
        self.assertEqual(record["bytes"], 0)
        self.assertEqual(record["sha256"], "")
        record = ledger.classify_source(
            {
                "id": "PDF2",
                "download_url": "https://example.org/b.pdf",
                "previous_recovery": {"bytes": 123, "sha256": "a" * 64, "package": "archive.zip"},
            },
            ROOT / "dados" / "recovery",
        )
        self.assertEqual(record["bytes"], 123)
        self.assertEqual(record["sha256"], "a" * 64)
        self.assertIn("archive.zip", record["notes"])

    def test_local_archive_is_hashed_and_marked_preserved(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            relative = str((Path(tmp) / "sample.txt").relative_to(ROOT))
            file_path = ROOT / relative
            file_path.write_bytes(b"HAGF archive test")
            try:
                record = ledger.classify_source(
                    {"id": "LOCAL1", "archive_path": relative},
                    ROOT / "dados" / "recovery",
                )
                self.assertEqual(record["status"], "PRESERVED")
                self.assertEqual(record["bytes"], len(b"HAGF archive test"))
                self.assertEqual(len(record["sha256"]), 64)
            finally:
                file_path.unlink()

    def test_path_traversal_is_blocked(self):
        record = ledger.classify_source(
            {"id": "BAD1", "archive_path": "../../outside.txt"},
            ROOT / "dados" / "recovery",
        )
        self.assertEqual(record["status"], "BLOCKED_PATH_TRAVERSAL")

    def test_ledger_counts_all_sources(self):
        manifest = json.loads((ROOT / "config" / "fontes_publicas.json").read_text(encoding="utf-8"))
        result = ledger.build_ledger(manifest, ROOT / "dados" / "recovery")
        self.assertEqual(result["source_count"], len(manifest["sources"]))
        self.assertEqual(result["source_count"], 23)


if __name__ == "__main__":
    unittest.main()
