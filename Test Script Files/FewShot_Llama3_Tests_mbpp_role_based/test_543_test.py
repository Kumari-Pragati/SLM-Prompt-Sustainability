import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(count_digits(1, 2), 2)

    def test_multiple_digits(self):
        self.assertEqual(count_digits(123, 456), 3)

    def test_zero(self):
        self.assertEqual(count_digits(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_digits(-1, 2), 2)

    def test_mixed_signs(self):
        self.assertEqual(count_digits(-1, 2), 2)

    def test_large_numbers(self):
        self.assertEqual(count_digits(123456, 789012), 7)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            count_digits('abc', 123)
