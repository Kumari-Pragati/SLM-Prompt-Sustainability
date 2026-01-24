import unittest
from mbpp_566_code import sum_digits

class TestSumDigits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(sum_digits(0), 0)

    def test_single_digit(self):
        self.assertEqual(sum_digits(1), 1)
        self.assertEqual(sum_digits(2), 2)
        self.assertEqual(sum_digits(3), 3)
        self.assertEqual(sum_digits(4), 4)
        self.assertEqual(sum_digits(5), 5)
        self.assertEqual(sum_digits(6), 6)
        self.assertEqual(sum_digits(7), 7)
        self.assertEqual(sum_digits(8), 8)
        self.assertEqual(sum_digits(9), 9)

    def test_positive_numbers(self):
        self.assertEqual(sum_digits(10), 1)
        self.assertEqual(sum_digits(123), 6)
        self.assertEqual(sum_digits(456), 15)
        self.assertEqual(sum_digits(789), 24)

    def test_negative_numbers(self):
        self.assertEqual(sum_digits(-10), 1)
        self.assertEqual(sum_digits(-123), 6)
        self.assertEqual(sum_digits(-456), 15)
        self.assertEqual(sum_digits(-789), 24)

    def test_large_numbers(self):
        self.assertEqual(sum_digits(1000), 1)
        self.assertEqual(sum_digits(123456), 21)
        self.assertEqual(sum_digits(987654321), 45)

    def test_edge_cases(self):
        self.assertEqual(sum_digits(-0), 0)
        self.assertEqual(sum_digits(0.0), 0)
        self.assertEqual(sum_digits(-0.0), 0)
