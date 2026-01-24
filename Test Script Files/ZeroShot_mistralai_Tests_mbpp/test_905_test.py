import unittest
from mbpp_905_code import sum_of_square, factorial

class TestSumOfSquare(unittest.TestCase):

    def test_sum_of_square_with_positive_integer(self):
        self.assertEqual(sum_of_square(1), 1)
        self.assertEqual(sum_of_square(2), 5)
        self.assertEqual(sum_of_square(3), 14)
        self.assertEqual(sum_of_square(4), 30)
        self.assertEqual(sum_of_square(5), 52)

    def test_sum_of_square_with_zero(self):
        self.assertEqual(sum_of_square(0), 0)

    def test_sum_of_square_with_negative_integer(self):
        self.assertEqual(sum_of_square(-1), -1)

    def test_sum_of_square_with_large_integer(self):
        self.assertEqual(sum_of_square(100), 25462690987484987)
