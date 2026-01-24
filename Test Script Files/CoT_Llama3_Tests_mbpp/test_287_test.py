import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):
    def test_square_sum_positive(self):
        self.assertEqual(square_Sum(1), 2)
        self.assertEqual(square_Sum(2), 20)
        self.assertEqual(square_Sum(3), 70)

    def test_square_sum_negative(self):
        with self.assertRaises(TypeError):
            square_Sum(-1)

    def test_square_sum_zero(self):
        self.assertEqual(square_Sum(0), 0)

    def test_square_sum_non_integer(self):
        with self.assertRaises(TypeError):
            square_Sum(1.5)

    def test_square_sum_large(self):
        self.assertEqual(square_Sum(100), 124000)
