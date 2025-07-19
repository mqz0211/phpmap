import unittest
from phpmap import lfi_module

class TestLFIModule(unittest.TestCase):
    def test_lfi_scans_runs_without_crash(self):
        """Test that LFI module runs without throwing exceptions."""
        try:
            lfi_module("http://example.com/vuln.php")
        except Exception as e:
            self.fail(f"LFI scan crashed: {e}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
