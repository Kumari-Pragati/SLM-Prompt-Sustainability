import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(square_Sum(1), 6)
        self.assertEqual(square_Sum(2), 28)
        self.assertEqual(square_Sum(3), 81)

    def test_edge_case_zero(self):
        self.assertEqual(square_Sum(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(square_Sum(1), 6)

    def test_boundary_case_min_positive(self):
        self.assertEqual(square_Sum(1), 6)

    def test_boundary_case_max_positive(self):
        self.assertEqual(square_Sum(10000), 333333338)
