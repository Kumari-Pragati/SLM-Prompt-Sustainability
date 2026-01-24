import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):
    def test_match_5_string(self):
        self.assertTrue(match_num("5"))

    def test_match_5_at_start_of_string(self):
        self.assertTrue(match_num("5abc"))

    def test_match_5_at_end_of_string(self):
        self.assertTrue(match_num("ab5"))

    def test_match_5_in_middle_of_string(self):
        self.assertFalse(match_num("abc5def"))

    def test_match_non_5_string(self):
        self.assertFalse(match_num("4"))

    def test_match_empty_string(self):
        self.assertFalse(match_num(""))

    def test_match_whitespace_string(self):
        self.assertFalse(match_num("   "))
