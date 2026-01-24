import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):

    def test_simple_case_1(self):
        self.assertTrue(check_Validity(1, 1, 2))

    def test_simple_case_2(self):
        self.assertTrue(check_Validity(2, 1, 3))

    def test_simple_case_3(self):
        self.assertTrue(check_Validity(3, 1, 4))

    def test_simple_case_4(self):
        self.assertTrue(check_Validity(1, 2, 3))

    def test_edge_case_1(self):
        self.assertTrue(check_Validity(1, 1, 2))

    def test_edge_case_2(self):
        self.assertTrue(check_Validity(2, 1, 2))

    def test_edge_case_3(self):
        self.assertTrue(check_Validity(1, 2, 2))

    def test_boundary_case_1(self):
        self.assertTrue(check_Validity(sys.maxsize // 2, sys.maxsize // 2, sys.maxsize))

    def test_boundary_case_2(self):
        self.assertTrue(check_Validity(sys.maxsize, sys.maxsize // 2, sys.maxsize // 2))

    def test_boundary_case_3(self):
        self.assertTrue(check_Validity(sys.maxsize // 2, sys.maxsize, sys.maxsize // 2))

    def test_negative_case_1(self):
        self.assertFalse(check_Validity(-1, 1, 2))

    def test_negative_case_2(self):
        self.assertFalse(check_Validity(1, -1, 2))

    def test_negative_case_3(self):
        self.assertFalse(check_Validity(1, 1, -1))
