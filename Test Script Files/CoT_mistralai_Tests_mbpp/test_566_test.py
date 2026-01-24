import unittest
from mbpp_566_code import sum_digits

class TestSumDigits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(sum_digits(0), 0)

    def test_positive_numbers(self):
        for n in range(1, 100):
            self.assertEqual(sum_digits(n), sum(int(digit) for digit in str(n)))

    def test_large_number(self):
        self.assertEqual(sum_digits(1234567890), 45)

    def test_negative_numbers(self):
        for n in range(-1, -10, -1):
            self.assertEqual(sum_digits(n), sum(int(digit) for digit in str(abs(n))))

    def test_float(self):
        with self.assertRaises(TypeError):
            sum_digits(3.14)

    def test_string(self):
        with self.assertRaises(TypeError):
            sum_digits('abc')

    def test_empty(self):
        with self.assertRaises(ZeroDivisionError):
            sum_digits(0)
