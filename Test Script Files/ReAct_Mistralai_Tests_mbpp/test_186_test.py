import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):

    def test_matches_single_pattern(self):
        self.assertEqual(check_literals("Hello, World!", r"World"), "Matched!")

    def test_matches_multiple_patterns(self):
        self.assertEqual(check_literals("Python 3.9.2", r"Python", r"3"), "Matched! Matched!")

    def test_no_matches(self):
        self.assertEqual(check_literals("Hello, World!", r"Goodbye"), "Not Matched!")

    def test_empty_text(self):
        self.assertEqual(check_literals("", r"World"), "Not Matched!")

    def test_empty_pattern(self):
        self.assertEqual(check_literals("Hello, World!", ""), "Not Matched!")

    def test_non_string_text(self):
        with self.assertRaises(TypeError):
            check_literals(123, r"World")

    def test_non_string_pattern(self):
        with self.assertRaises(TypeError):
            check_literals("Hello, World!", 123)
