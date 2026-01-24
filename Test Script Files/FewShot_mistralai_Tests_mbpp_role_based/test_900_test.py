import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):
    def test_match_5(self):
        self.assertTrue(match_num("5"))

    def test_match_5_with_leading_spaces(self):
        self.assertTrue(match_num("  5"))

    def test_match_5_with_leading_zeros(self):
        self.assertTrue(match_num("00005"))

    def test_non_match_6(self):
        self.assertFalse(match_num("6"))

    def test_non_match_negative_number(self):
        self.assertFalse(match_num("-5"))

    def test_non_match_empty_string(self):
        self.assertFalse(match_num(""))

    def test_non_match_string_with_numbers(self):
        self.assertFalse(match_num("12345"))
