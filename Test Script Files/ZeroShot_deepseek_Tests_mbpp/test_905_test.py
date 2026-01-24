import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):

    def test_sum_of_square_positive(self):
        self.assertEqual(sum_of_square(1), 1)
        self.assertEqual(sum_of_square(2), 5)
        self.assertEqual(sum_of_square(3), 14)
        self.assertEqual(sum_of_square(4), 42)
        self.assertEqual(sum_of_square(5), 132)

    def test_sum_of_square_negative(self):
        self.assertEqual(sum_of_square(-1), 1)
        self.assertEqual(sum_of_square(-2), 5)
        self.assertEqual(sum_of_square(-3), 14)
        self.assertEqual(sum_of_square(-4), 42)
        self.assertEqual(sum_of_square(-5), 132)

    def test_sum_of_square_zero(self):
        self.assertEqual(sum_of_square(0), 1)

    def test_sum_of_square_large_number(self):
        self.assertEqual(sum_of_square(10), 3858)
