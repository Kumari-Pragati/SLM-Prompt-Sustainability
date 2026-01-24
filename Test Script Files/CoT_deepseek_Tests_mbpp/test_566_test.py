import unittest
from mbpp_566_code import sum_digits

class TestSumDigits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_digits(123), 6)
        self.assertEqual(sum_digits(456), 15)
        self.assertEqual(sum_digits(789), 24)

    def test_single_digit_numbers(self):
        for i in range(10):
            self.assertEqual(sum_digits(i), i)

    def test_zero(self):
        self.assertEqual(sum_digits(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_digits(-123), 6)
        self.assertEqual(sum_digits(-456), 15)
        self.assertEqual(sum_digits(-789), 24)

    def test_large_numbers(self):
        self.assertEqual(sum_digits(1000000000), 1)
        self.assertEqual(sum_digits(987654321), 45)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_digits('123')
        with self.assertRaises(TypeError):
            sum_digits([])
        with self.assertRaises(TypeError):
            sum_digits({})
