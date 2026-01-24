import unittest
from mbpp_566_code import sum_digits

class TestSumDigits(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(sum_digits(123), 6)
        self.assertEqual(sum_digits(4567), 24)
        self.assertEqual(sum_digits(987654), 21)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(sum_digits(0), 0)
        self.assertEqual(sum_digits(10), 1)
        self.assertEqual(sum_digits(100), 1)
        self.assertEqual(sum_digits(1000), 1)
        self.assertEqual(sum_digits(10000), 1)
        self.assertEqual(sum_digits(999999), 18)

    def test_negative_numbers(self):
        self.assertEqual(sum_digits(-123), 6)
        self.assertEqual(sum_digits(-4567), 11)
        self.assertEqual(sum_digits(-987654), 21)

    def test_large_positive_numbers(self):
        self.assertEqual(sum_digits(123456789), 45)
        self.assertEqual(sum_digits(1234567890), 45)
        self.assertEqual(sum_digits(12345678901), 56)
