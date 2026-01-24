import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_square_sum_positive(self):
        self.assertEqual(square_Sum(1), 1)

    def test_square_sum_negative(self):
        self.assertEqual(square_Sum(-1), -1)

    def test_square_sum_zero(self):
        self.assertEqual(square_Sum(0), 0)

    def test_square_sum_integer(self):
        self.assertEqual(square_Sum(2), 8)

    def test_square_sum_non_integer(self):
        self.assertAlmostEqual(square_Sum(2.5), 16.666666666666668)

    def test_square_sum_edge_case(self):
        self.assertEqual(square_Sum(1000), 1000)

    def test_square_sum_edge_case_negative(self):
        self.assertEqual(square_Sum(-1000), -1000)
