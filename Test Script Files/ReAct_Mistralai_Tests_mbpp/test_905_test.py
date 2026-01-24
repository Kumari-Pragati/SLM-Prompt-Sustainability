import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(sum_of_square(1), 1)
        self.assertEqual(sum_of_square(5), 6)
        self.assertEqual(sum_of_square(10), 120)

    def test_zero(self):
        self.assertEqual(sum_of_square(0), 0)

    def test_negative_integer(self):
        self.assertEqual(sum_of_square(-1), -1)

    def test_large_integer(self):
        self.assertEqual(sum_of_square(1000), 12676000000)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            sum_of_square(3.14)

    def test_negative_factorial(self):
        with self.assertRaises(ValueError):
            sum_of_square(-1, 1)
