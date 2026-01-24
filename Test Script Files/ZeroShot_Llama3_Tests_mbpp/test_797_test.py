import unittest
from mbpp_797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):

    def test_sum_in_Range(self):
        self.assertEqual(sum_in_Range(1, 1), 0)
        self.assertEqual(sum_in_Range(1, 2), 1)
        self.assertEqual(sum_in_Range(1, 3), 3)
        self.assertEqual(sum_in_Range(1, 4), 6)
        self.assertEqual(sum_in_Range(1, 5), 9)
        self.assertEqual(sum_in_Range(1, 6), 12)
        self.assertEqual(sum_in_Range(1, 7), 15)
        self.assertEqual(sum_in_Range(1, 8), 21)
        self.assertEqual(sum_in_Range(1, 9), 25)
        self.assertEqual(sum_in_Range(1, 10), 30)

    def test_sum_in_Range_negative(self):
        self.assertEqual(sum_in_Range(-1, -1), 0)
        self.assertEqual(sum_in_Range(-1, -2), -1)
        self.assertEqual(sum_in_Range(-1, -3), -3)
        self.assertEqual(sum_in_Range(-1, -4), -6)
        self.assertEqual(sum_in_Range(-1, -5), -9)
        self.assertEqual(sum_in_Range(-1, -6), -12)
        self.assertEqual(sum_in_Range(-1, -7), -15)
        self.assertEqual(sum_in_Range(-1, -8), -21)
        self.assertEqual(sum_in_Range(-1, -9), -25)
        self.assertEqual(sum_in_Range(-1, -10), -30)

    def test_sum_in_Range_zero(self):
        self.assertEqual(sum_in_Range(0, 0), 0)
        self.assertEqual(sum_in_Range(0, 1), 1)
        self.assertEqual(sum_in_Range(0, 2), 3)
        self.assertEqual(sum_in_Range(0, 3), 6)
        self.assertEqual(sum_in_Range(0, 4), 9)
        self.assertEqual(sum_in_Range(0, 5), 12)
        self.assertEqual(sum_in_Range(0, 6), 15)
        self.assertEqual(sum_in_Range(0, 7), 21)
        self.assertEqual(sum_in_Range(0, 8), 25)
        self.assertEqual(sum_in_Range(0, 9), 30)

    def test_sum_in_Range_positive(self):
        self.assertEqual(sum_in_Range(1, 2), 1)
        self.assertEqual(sum_in_Range(1, 3), 3)
        self.assertEqual(sum_in_Range(1, 4), 6)
        self.assertEqual(sum_in_Range(1, 5), 9)
        self.assertEqual(sum_in_Range(1, 6), 12)
        self.assertEqual(sum_in_Range(1, 7), 15)
        self.assertEqual(sum_in_Range(1, 8), 21)
        self.assertEqual(sum_in_Range(1, 9), 25)
        self.assertEqual(sum_in_Range(1, 10), 30)
