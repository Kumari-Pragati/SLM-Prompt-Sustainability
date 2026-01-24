import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_square_sum_positive(self):
        self.assertEqual(square_Sum(1), 1)

    def test_square_sum_negative(self):
        self.assertEqual(square_Sum(-1), -1)

    def test_square_sum_zero(self):
        self.assertEqual(square_Sum(0), 0)

    def test_square_sum_non_integer(self):
        with self.assertRaises(TypeError):
            square_Sum(1.5)

    def test_square_sum_large(self):
        self.assertEqual(square_Sum(1000), 1000**3)

    def test_square_sum_edge_case(self):
        self.assertEqual(square_Sum(1e6), 1e12)
