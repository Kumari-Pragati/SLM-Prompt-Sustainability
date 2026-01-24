import unittest
from mbpp_566_code import Union

from 566_code import sum_digits

class TestSumDigits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(sum_digits(0), 0)

    def test_positive_numbers(self):
        for num in [1, 12, 123, 1234, 12345]:
            self.assertEqual(sum_digits(num), sum(int(digit) for digit in str(num)))

    def test_negative_numbers(self):
        for num in [-1, -12, -123, -1234, -12345]:
            self.assertEqual(sum_digits(num), sum(int(digit) for digit in str(abs(num))))

    def test_floats(self):
        for num in [1.23, -1.23, 123.456]:
            self.assertAlmostEqual(sum_digits(num), sum(int(digit) for digit in str(int(num))))

    def test_strings(self):
        for string in ['1', '12', '123', '1234', '12345']:
            self.assertEqual(sum_digits(string), sum(int(digit) for digit in string))

    def test_non_numeric_strings(self):
        for string in ['abc', '1a', 'a1', 'abcd', '1234ab']:
            with self.assertRaises(ValueError):
                sum_digits(string)
