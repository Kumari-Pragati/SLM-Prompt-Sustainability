import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_square_sum_positive(self):
        self.assertEqual(square_Sum(1), 2)

    def test_square_sum_zero(self):
        self.assertEqual(square_Sum(0), 0)

    def test_square_sum_negative(self):
        self.assertEqual(square_Sum(-1), 2)

    def test_square_sum_edge(self):
        self.assertEqual(square_Sum(100), 125000)

    def test_square_sum_non_integer(self):
        with self.assertRaises(TypeError):
            square_Sum(1.5)

    def test_square_sum_non_numeric(self):
        with self.assertRaises(TypeError):
            square_Sum('a')
