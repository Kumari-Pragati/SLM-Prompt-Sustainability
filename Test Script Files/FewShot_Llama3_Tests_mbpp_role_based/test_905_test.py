import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(sum_of_square(2), 5)

    def test_zero(self):
        with self.assertRaises(ValueError):
            sum_of_square(0)

    def test_negative_integer(self):
        with self.assertRaises(ValueError):
            sum_of_square(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            sum_of_square('a')

    def test_edge_case(self):
        self.assertEqual(sum_of_square(1), 1)

    def test_large_integer(self):
        self.assertEqual(sum_of_square(10), 385)
