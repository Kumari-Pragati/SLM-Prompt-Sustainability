import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):
    def test_match_5(self):
        self.assertTrue(match_num("5"))

    def test_match_5_start(self):
        self.assertTrue(match_num("5abc"))

    def test_match_5_end(self):
        self.assertTrue(match_num("a5"))

    def test_match_5_middle(self):
        self.assertTrue(match_num("123567"))

    def test_no_match_non_5(self):
        self.assertFalse(match_num("4"))

    def test_no_match_non_5_start(self):
        self.assertFalse(match_num("4abc"))

    def test_no_match_non_5_end(self):
        self.assertFalse(match_num("a4"))

    def test_no_match_non_5_middle(self):
        self.assertFalse(match_num("123467"))

    def test_no_match_empty_string(self):
        self.assertFalse(match_num(""))

    def test_no_match_non_string(self):
        self.assertRaises(TypeError, match_num, 123)
