import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):
    def test_valid_input(self):
        self.assertTrue(check_Validity(1, 2, 3))

    def test_invalid_input1(self):
        self.assertFalse(check_Validity(1, 1, 1))

    def test_invalid_input2(self):
        self.assertFalse(check_Validity(1, 2, 1))

    def test_invalid_input3(self):
        self.assertFalse(check_Validity(1, 1, 2))

    def test_edge_case1(self):
        self.assertTrue(check_Validity(1, 2, 3))

    def test_edge_case2(self):
        self.assertTrue(check_Validity(2, 3, 1))

    def test_edge_case3(self):
        self.assertTrue(check_Validity(3, 1, 2))

    def test_edge_case4(self):
        self.assertTrue(check_Validity(1, 1, 2))

    def test_edge_case5(self):
        self.assertTrue(check_Validity(2, 2, 2))

    def test_edge_case6(self):
        self.assertTrue(check_Validity(3, 3, 3))

    def test_edge_case7(self):
        self.assertTrue(check_Validity(1, 3, 2))

    def test_edge_case8(self):
        self.assertTrue(check_Validity(2, 1, 3))

    def test_edge_case9(self):
        self.assertTrue(check_Validity(3, 2, 1))

    def test_edge_case10(self):
        self.assertTrue(check_Validity(1, 1, 1))

    def test_edge_case11(self):
        self.assertTrue(check_Validity(2, 2, 2))

    def test_edge_case12(self):
        self.assertTrue(check_Validity(3, 3, 3))
