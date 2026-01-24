import unittest
from mbpp_566_code import sum_digits

class TestSumDigits(unittest.TestCase):

    def test_sum_digits(self):
        self.assertEqual(sum_digits(0), 0)
        self.assertEqual(sum_digits(123), 6)
        self.assertEqual(sum_digits(456), 15)
        self.assertEqual(sum_digits(789), 21)
        self.assertEqual(sum_digits(12345), 15)
        self.assertEqual(sum_digits(-123), 6)
        self.assertEqual(sum_digits(123456789), 45)
        self.assertEqual(sum_digits(-123456789), 45)
        self.assertEqual(sum_digits(1000000003), 6)
        self.assertEqual(sum_digits(-1000000003), 6)

    def test_sum_digits_edge_cases(self):
        self.assertEqual(sum_digits(0), 0)
        self.assertEqual(sum_digits(-0), 0)
        self.assertEqual(sum_digits(1), 1)
        self.assertEqual(sum_digits(-1), 1)
        self.assertEqual(sum_digits(10), 1)
        self.assertEqual(sum_digits(-10), 1)
