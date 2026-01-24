import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(sum_Of_Series(1), 1)
        self.assertEqual(sum_Of_Series(2), 8)
        self.assertEqual(sum_Of_Series(3), 33)
        self.assertEqual(sum_Of_Series(4), 104)
        self.assertEqual(sum_Of_Series(5), 275)

    def test_zero(self):
        self.assertEqual(sum_Of_Series(0), 0)

    def test_negative_integer(self):
        self.assertEqual(sum_Of_Series(-1), -1)
        self.assertEqual(sum_Of_Series(-2), -64)
        self.assertEqual(sum_Of_Series(-3), -273)
        self.assertEqual(sum_Of_Series(-4), -1024)
        self.assertEqual(sum_Of_Series(-5), -3375)
