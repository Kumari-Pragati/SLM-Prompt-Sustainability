import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):

    def test_match_5(self):
        self.assertTrue(match_num("5"))

    def test_match_5_start(self):
        self.assertTrue(match_num("5abc"))

    def test_match_5_leading_spaces(self):
        self.assertTrue(match_num(" 5"))

    def test_match_5_leading_zero(self):
        self.assertTrue(match_num("05"))

    def test_match_5_multiple_digits(self):
        self.assertTrue(match_num("12345"))

    def test_non_match_6(self):
        self.assertFalse(match_num("6"))

    def test_non_match_5_with_leading_char(self):
        self.assertFalse(match_num("a5"))

    def test_non_match_non_number(self):
        self.assertFalse(match_num("abc"))

    def test_non_match_empty_string(self):
        self.assertFalse(match_num(""))
