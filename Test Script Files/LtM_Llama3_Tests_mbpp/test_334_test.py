import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(check_Validity(1, 2, 3))

    def test_simple_invalid(self):
        self.assertFalse(check_Validity(1, 2, 1))

    def test_edge_case1(self):
        self.assertFalse(check_Validity(1, 1, 2))

    def test_edge_case2(self):
        self.assertFalse(check_Validity(1, 2, 1))

    def test_edge_case3(self):
        self.assertFalse(check_Validity(1, 1, 1))

    def test_edge_case4(self):
        self.assertFalse(check_Validity(2, 1, 1))

    def test_edge_case5(self):
        self.assertFalse(check_Validity(1, 1, 0))

    def test_edge_case6(self):
        self.assertFalse(check_Validity(0, 1, 1))

    def test_edge_case7(self):
        self.assertFalse(check_Validity(1, 0, 1))

    def test_edge_case8(self):
        self.assertFalse(check_Validity(0, 0, 1))
