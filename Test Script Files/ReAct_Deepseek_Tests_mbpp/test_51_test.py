import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_equilateral(3, 3, 3))

    def test_edge_case_with_zero(self):
        self.assertFalse(check_equilateral(0, 0, 0))

    def test_edge_case_with_negative_numbers(self):
        self.assertFalse(check_equilateral(-1, -1, -1))

    def test_edge_case_with_one_positive_one_negative(self):
        self.assertFalse(check_equilateral(1, -1, 1))

    def test_edge_case_with_different_numbers(self):
        self.assertFalse(check_equilateral(1, 2, 3))
