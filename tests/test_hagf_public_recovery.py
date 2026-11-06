import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import hagf_public_recovery as recovery


class PublicRecoveryTests(unittest.TestCase):
    def test_https_allowlisted_host_is_accepted(self):
        ok, reason = recovery.validate_url(
            "https://lp.agf.com.br/documento.pdf",
            ["lp.agf.com.br", "agf.com.br"],
        )
        self.assertTrue(ok)
        self.assertEqual(reason, "OK")

    def test_non_https_is_rejected(self):
        ok, reason = recovery.validate_url(
            "http://lp.agf.com.br/documento.pdf",
            ["lp.agf.com.br"],
        )
        self.assertFalse(ok)
        self.assertEqual(reason, "BLOCKED_NON_HTTPS")

    def test_non_allowlisted_host_is_rejected(self):
        ok, reason = recovery.validate_url(
            "https://example.org/documento.pdf",
            ["lp.agf.com.br"],
        )
        self.assertFalse(ok)
        self.assertEqual(reason, "BLOCKED_HOST_NOT_ALLOWLISTED")

    def test_credentials_in_url_are_rejected(self):
        ok, reason = recovery.validate_url(
            "https://user:secret@lp.agf.com.br/documento.pdf",
            ["lp.agf.com.br"],
        )
        self.assertFalse(ok)
        self.assertEqual(reason, "BLOCKED_CREDENTIALS_IN_URL")

    def test_filename_is_sanitized(self):
        self.assertEqual(recovery.safe_name("../../Politica de Privacidade.pdf"),
                         "Politica_de_Privacidade.pdf")

    def test_manifest_loads_in_expected_mode(self):
        old_config = recovery.CONFIG
        try:
            recovery.CONFIG = ROOT / "config" / "fontes_publicas.json"
            cfg = recovery.load_config()
            self.assertEqual(cfg["policy"]["mode"], "explicit_direct_download_only")
            self.assertTrue(any(s["id"] == "AGF_PRIVACY_PDF_2025" for s in cfg["sources"]))
        finally:
            recovery.CONFIG = old_config


if __name__ == "__main__":
    unittest.main()
