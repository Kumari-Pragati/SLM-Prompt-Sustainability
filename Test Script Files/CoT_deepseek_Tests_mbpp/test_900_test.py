import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(match_num("5"))
        self.assertTrue(match_num("5678"))

    def test_non_string_input(self):
        self.assertFalse(match_num(5))
        self.assertFalse(match_num(True))
        self.assertFalse(match_num(None))
        self.assertFalse(match_num(1234))

    def test_empty_string(self):
        self.assertFalse(match_num(""))

    def test_string_without_leading_5(self):
        self.assertFalse(match_num("6789"))
        self.assertFalse(match_num("abc"))
        self.assertFalse(match_num("1234"))

    def test_string_with_leading_5(self):
        self.assertTrue(match_num("5"))
        self.assertTrue(match_num("5678"))
        self.assertTrue(match_num("5abc"))
        self.assertTrue(match_num("51234"))
