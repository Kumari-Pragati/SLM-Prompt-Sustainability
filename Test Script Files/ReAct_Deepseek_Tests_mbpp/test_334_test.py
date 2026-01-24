import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_Validity(1, 2, 3))

    def test_edge_case_with_zero(self):
        self.assertTrue(check_Validity(0, 0, 0))

    def test_edge_case_with_negative_numbers(self):
        self.assertTrue(check_Validity(-1, -2, -3))

    def test_edge_case_with_one_zero(self):
        self.assertFalse(check_Validity(0, 1, 2))

    def test_edge_case_with_two_zeros(self):
        self.assertFalse(check_Validity(0, 0, 1))

    def test_edge_case_with_two_equal_sides(self):
        self.assertFalse(check_Validity(2, 2, 3))

    def test_edge_case_with_two_equal_sides_and_zero(self):
        self.assertFalse(check_Validity(0, 2, 2))

    def test_edge_case_with_two_equal_sides_and_negative_numbers(self):
        self.assertFalse(check_Validity(-2, -2, 3))

    def test_edge_case_with_two_equal_sides_and_one_zero(self):
        self.assertFalse(check_Validity(0, 2, 2))

    def test_edge_case_with_two_equal_sides_and_two_zeros(self):
        self.assertFalse(check_Validity(0, 0, 2))
