import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(match_num("5"))
        self.assertTrue(match_num("50"))
        self.assertTrue(match_num("500"))

    def test_edge_conditions(self):
        self.assertTrue(match_num("5"))
        self.assertFalse(match_num("6"))
        self.assertFalse(match_num(""))

    def test_boundary_conditions(self):
        self.assertTrue(match_num("5" * 1000))
        self.assertFalse(match_num("6" * 1000))

    def test_invalid_inputs(self):
        self.assertFalse(match_num("65"))
        self.assertFalse(match_num("56"))
        self.assertFalse(match_num("abc"))
        self.assertFalse(match_num("123"))
