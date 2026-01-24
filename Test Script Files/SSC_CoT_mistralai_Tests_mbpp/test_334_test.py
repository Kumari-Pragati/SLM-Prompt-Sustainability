import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):

    def test_normal_case(self):
        self.assertTrue(check_Validity(1, 2, 3))
        self.assertTrue(check_Validity(2, 3, 4))
        self.assertTrue(check_Validity(3, 4, 5))
        self.assertTrue(check_Validity(4, 5, 6))
        self.assertTrue(check_Validity(5, 6, 7))

    def test_edge_case_1(self):
        self.assertTrue(check_Validity(1, 2, 2))
        self.assertTrue(check_Validity(2, 2, 3))
        self.assertTrue(check_Validity(3, 3, 4))

    def test_edge_case_2(self):
        self.assertTrue(check_Validity(0, 1, 2))
        self.assertTrue(check_Validity(1, 0, 2))
        self.assertTrue(check_Validity(1, 2, 0))

    def test_edge_case_3(self):
        self.assertTrue(check_Validity(1, 1.5, 2))
        self.assertTrue(check_Validity(1, 2, 1.5))
        self.assertTrue(check_Validity(1.5, 2, 1))

    def test_invalid_inputs(self):
        self.assertFalse(check_Validity(0, 0, 0))
        self.assertFalse(check_Validity(None, None, None))
        self.assertFalse(check_Validity('a', 'b', 'c'))
        self.assertFalse(check_Validity([1, 2, 3], [4, 5, 6], [7, 8, 9]))
