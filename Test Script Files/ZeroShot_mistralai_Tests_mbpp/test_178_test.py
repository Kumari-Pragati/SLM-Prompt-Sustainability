import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):

    def test_empty_patterns(self):
        self.assertEqual(string_literals([], "test"), "Not Matched!")

    def test_single_pattern(self):
        self.assertEqual(string_literals(["pattern"], "test"), "Not Matched!" if "pattern" not in "test" else "Matched!")

    def test_multiple_patterns(self):
        self.assertEqual(string_literals(["pattern1", "pattern2"], "test"), "Not Matched!" if not (("pattern1" in "test") or ("pattern2" in "test")) else "Matched!")

    def test_case_insensitive_patterns(self):
        self.assertEqual(string_literals(["PATTERN"], "test"), "Not Matched!" if "PATTERN" not in "test" else "Matched!")

    def test_pattern_with_spaces(self):
        self.assertEqual(string_literals(["pattern with spaces"], "test with spaces"), "Matched!")
