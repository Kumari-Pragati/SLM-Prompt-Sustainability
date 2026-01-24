import unittest
from962_code import sum_Even

class TestSumEven(unittest.TestCase):

    def test_sum_even_with_positive_numbers(self):
        self.assertEqual(sum_Even(2, 4), 6)
        self.assertEqual(sum_Even(4, 6), 12)
        self.assertEqual(sum_Even(6, 8), 20)

    def test_sum_even_with_negative_numbers(self):
        self.assertEqual(sum_Even(-2, -4), 6)
        self.assertEqual(sum_Even(-4, -6), 12)
        self.assertEqual(sum_Even(-6, -8), 20)

    def test_sum_even_with_zero(self):
        self.assertEqual(sum_Even(0, 2), 0)
        self.assertEqual(sum_Even(2, 0), 0)

    def test_sum_even_with_one_argument(self):
        with self.assertRaises(TypeError):
            sum_Even(2)
        with self.assertRaises(TypeError):
            sum_Even('str')

    def test_sum_even_with_invalid_arguments(self):
        with self.assertRaises(ValueError):
            sum_Even(-1, 0)
        with self.assertRaises(ValueError):
            sum_Even(0, -1)
