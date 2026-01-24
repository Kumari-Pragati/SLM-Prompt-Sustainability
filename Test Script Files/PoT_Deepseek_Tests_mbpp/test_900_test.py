import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(match_num("5"))
        self.assertTrue(match_num("50"))
        self.assertTrue(match_num("500"))
        self.assertTrue(match_num("5000"))

    def test_edge_cases(self):
        self.assertTrue(match_num("5"))
        self.assertFalse(match_num(""))
        self.assertFalse(match_num("4"))
        self.assertFalse(match_num("6"))

    def test_corner_cases(self):
        self.assertTrue(match_num("55"))
        self.assertFalse(match_num("54"))
        self.assertFalse(match_num("45"))
        self.assertFalse(match_num("65"))
