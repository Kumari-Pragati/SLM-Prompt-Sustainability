import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(max_run_uppercase(""), 0)

    def test_single_uppercase(self):
        self.assertEqual(max_run_uppercase("A"), 1)

    def test_single_lowercase(self):
        self.assertEqual(max_run_uppercase("a"), 0)

    def test_multiple_uppercase(self):
        self.assertEqual(max_run_uppercase("ABC"), 3)

    def test_multiple_lowercase(self):
        self.assertEqual(max_run_uppercase("abc"), 0)

    def test_mixed_uppercase_lowercase(self):
        self.assertEqual(max_run_uppercase("AbC"), 3)

    def test_long_string(self):
        self.assertEqual(max_run_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)

    def test_long_string_with_spaces(self):
        self.assertEqual(max_run_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ "), 26)

    def test_long_string_with_spaces_and_punctuation(self):
        self.assertEqual(max_run_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ!"), 26)
