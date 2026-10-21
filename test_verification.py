"""Exercise the verification command using isolated synthetic CSV files."""
import csv
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


class VerificationTests(unittest.TestCase):
    def run_verifier(self, expected, actual, actual_fields=None):
        fields = ["case_id", "decision", "sequence", "owner"]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data").mkdir()
            (root / "results").mkdir()
            shutil.copyfile(Path(__file__).with_name("verify_sample.py"), root / "verify_sample.py")
            for path, rows, headers in [
                (root / "data/expected.csv", expected, fields),
                (root / "results/actual.csv", actual, actual_fields or fields),
            ]:
                with path.open("w", newline="", encoding="utf-8") as stream:
                    writer = csv.DictWriter(stream, fieldnames=headers)
                    writer.writeheader()
                    writer.writerows(rows)
            result = subprocess.run([sys.executable, str(root / "verify_sample.py")],
                                    capture_output=True, text=True, timeout=10)
            report = root / "results/verification.md"
            return result, report.read_text(encoding="utf-8") if report.exists() else ""

    def test_empty_expectations_cannot_pass(self):
        result, report = self.run_verifier([], [])
        self.assertEqual(result.returncode, 1)
        self.assertIn("No expected cases", result.stdout)
        self.assertIn("No expected cases", report)

    def test_missing_output_column_still_writes_failure_report(self):
        expected = [dict(case_id="a", decision="qualified", sequence="growth", owner="sales_queue")]
        result, report = self.run_verifier(expected, [dict(case_id="a", owner="sales_queue")],
                                           ["case_id", "owner"])
        self.assertEqual(result.returncode, 1)
        self.assertNotIn("Traceback", result.stderr)
        self.assertIn("FAIL", report)
        self.assertIn("decision", result.stdout)

    def test_row_count_failure_is_visible_in_report(self):
        expected = [dict(case_id="a", decision="qualified", sequence="growth", owner="sales_queue")]
        result, report = self.run_verifier(expected, [])
        self.assertEqual(result.returncode, 1)
        self.assertIn("Row count differs", report)

    def test_matching_case_passes(self):
        rows = [dict(case_id="a", decision="qualified", sequence="growth", owner="sales_queue")]
        result, report = self.run_verifier(rows, rows)
        self.assertEqual(result.returncode, 0)
        self.assertIn("PASS: 1/1", result.stdout)
        self.assertIn("PASS", report)


if __name__ == "__main__":
    unittest.main()
