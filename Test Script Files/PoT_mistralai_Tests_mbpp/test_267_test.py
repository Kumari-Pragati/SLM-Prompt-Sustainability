import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(square_Sum(3), 36)
        self.assertEqual(square_Sum(4), 64)
        self.assertEqual(square_Sum(5), 100)

    def test_edge_case_zero(self):
        self.assertEqual(square_Sum(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(square_Sum(1), 1)

    def test_edge_case_negative(self):
        self.assertRaises(ValueError, square_Sum, -1)
