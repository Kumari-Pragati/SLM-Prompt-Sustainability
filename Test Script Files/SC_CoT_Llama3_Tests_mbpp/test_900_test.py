import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):

    def test_match_num_typical(self):
        self.assertTrue(match_num("5hello"))

    def test_match_num_non_match(self):
        self.assertFalse(match_num("hello"))

    def test_match_num_edge_case(self):
        self.assertTrue(match_num("5"))

    def test_match_num_edge_case2(self):
        self.assertFalse(match_num(""))

    def test_match_num_edge_case3(self):
        self.assertFalse(match_num("123"))

    def test_match_num_edge_case4(self):
        self.assertFalse(match_num("5abc"))

    def test_match_num_edge_case5(self):
        self.assertFalse(match_num("abc5"))

    def test_match_num_edge_case6(self):
        self.assertFalse(match_num("abc"))

    def test_match_num_edge_case7(self):
        self.assertFalse(match_num("5.5"))

    def test_match_num_edge_case8(self):
        self.assertFalse(match_num("5.5abc"))

    def test_match_num_edge_case9(self):
        self.assertFalse(match_num("abc5.5"))
