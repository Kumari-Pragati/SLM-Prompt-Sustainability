import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):
    def test_sum_of_square_positive(self):
        self.assertEqual(sum_of_square(1), 1)
        self.assertEqual(sum_of_square(2), 5)
        self.assertEqual(sum_of_square(3), 14)

    def test_sum_of_square_negative(self):
        with self.assertRaises(ValueError):
            sum_of_square(-1)

    def test_sum_of_square_zero(self):
        with self.assertRaises(ValueError):
            sum_of_square(0)

    def test_sum_of_square_large(self):
        self.assertEqual(sum_of_square(10), 385)

    def test_sum_of_square_invalid_type(self):
        with self.assertRaises(TypeError):
            sum_of_square("a")
