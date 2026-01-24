import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_of_square(5), 14)

    def test_small_number(self):
        self.assertEqual(sum_of_square(1), 1)

    def test_zero(self):
        self.assertEqual(sum_of_square(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            sum_of_square(-1)

    def test_large_number(self):
        with self.assertRaises(OverflowError):
            sum_of_square(1000)
