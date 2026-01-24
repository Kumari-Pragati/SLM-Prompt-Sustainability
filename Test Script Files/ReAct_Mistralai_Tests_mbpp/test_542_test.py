import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(fill_spaces(""), ":")

    def test_single_space(self):
        self.assertEqual(fill_spaces(" "), ":")

    def test_single_comma(self):
        self.assertEqual(fill_spaces(","), ":")

    def test_single_period(self):
        self.assertEqual(fill_spaces("."), ":")

    def test_multiple_spaces(self):
        self.assertEqual(fill_spaces("   "), ":")

    def test_multiple_commas(self):
        self.assertEqual(fill_spaces(",,,,"), ":,,:")

    def test_multiple_periods(self):
        self.assertEqual(fill_spaces("...."), ":....")

    def test_mixed_punctuation(self):
        self.assertEqual(fill_spaces(", .,"), ":.:")

    def test_leading_trailing_spaces(self):
        self.assertEqual(fill_spaces(" a b c   "), ":a:b:c:")

    def test_leading_trailing_punctuation(self):
        self.assertEqual(fill_spaces(",a.b,c,"), ":a.:b:c:")

    def test_error_non_string(self):
        with self.assertRaises(TypeError):
            fill_spaces(123)
