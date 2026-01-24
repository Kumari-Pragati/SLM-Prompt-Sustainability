import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(count_digits(123, 456), 6)
        self.assertEqual(count_digits(987654, 123456), 7)

    def test_zero(self):
        self.assertEqual(count_digits(0, 0), 1)

    def test_negative_numbers(self):
        self.assertEqual(count_digits(-123, -456), 5)
        self.assertEqual(count_digits(-987654, -123456), 7)

    def test_mixed_numbers(self):
        self.assertEqual(count_digits(-123, 456), 5)
        self.assertEqual(count_digits(123, -456), 5)

    def test_large_numbers(self):
        large_num = 12345678901234567890
        self.assertEqual(count_digits(large_num, 0), 21)
        self.assertEqual(count_digits(0, large_num), 21)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_digits, '123', 456)
        self.assertRaises(TypeError, count_digits, 123, '456')
