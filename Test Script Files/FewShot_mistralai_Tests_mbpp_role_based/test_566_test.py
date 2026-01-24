import unittest
from mbpp_566_code import sum_digits

class TestSumDigits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(sum_digits(0), 0)

    def test_single_digit(self):
        for num in range(1, 10):
            self.assertEqual(sum_digits(num), num)

    def test_multiple_digits(self):
        for num in range(10, 100):
            self.assertEqual(sum_digits(num), sum([int(digit) for digit in str(num)]))

    def test_large_number(self):
        for num in range(100, 1000):
            self.assertEqual(sum_digits(num), sum([int(digit) for digit in str(num)]))

    def test_negative_number(self):
        self.assertRaises(ValueError, sum_digits, -1)

    def test_floating_point_number(self):
        self.assertRaises(TypeError, sum_digits, 3.14)
