import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):

    def test_sum_of_square(self):
        self.assertEqual(sum_of_square(1), 1)
        self.assertEqual(sum_of_square(2), 5)
        self.assertEqual(sum_of_square(3), 14)
        self.assertEqual(sum_of_square(4), 30)
        self.assertEqual(sum_of_square(5), 55)
        self.assertEqual(sum_of_square(6), 91)
        self.assertEqual(sum_of_square(7), 140)
        self.assertEqual(sum_of_square(8), 203)
        self.assertEqual(sum_of_square(9), 285)
        self.assertEqual(sum_of_square(10), 385)
