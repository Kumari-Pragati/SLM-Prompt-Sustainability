import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):

    def test_sum_of_square_positive(self):
        self.assertEqual(sum_of_square(1), 1)

    def test_sum_of_square_negative(self):
        with self.assertRaises(ValueError):
            sum_of_square(-1)

    def test_sum_of_square_zero(self):
        self.assertEqual(sum_of_square(0), 0)

    def test_sum_of_square_small(self):
        self.assertEqual(sum_of_square(2), 5)

    def test_sum_of_square_large(self):
        self.assertEqual(sum_of_square(10), 385)
