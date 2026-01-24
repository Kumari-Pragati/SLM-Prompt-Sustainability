import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_single_digit_numbers(self):
        self.assertEqual(first_Digit(0), 0)
        self.assertEqual(first_Digit(5), 5)
        self.assertEqual(first_Digit(9), 9)

    def test_multiple_digit_numbers(self):
        self.assertEqual(first_Digit(123), 1)
        self.assertEqual(first_Digit(456), 4)
        self.assertEqual(first_Digit(789), 7)

    def test_negative_numbers(self):
        self.assertEqual(first_Digit(-123), 1)
        self.assertEqual(first_Digit(-456), 4)
        self.assertEqual(first_Digit(-789), 7)

    def test_large_numbers(self):
        self.assertEqual(first_Digit(123456789), 1)
        self.assertEqual(first_Digit(987654321), 9)

    def test_zero(self):
        self.assertEqual(first_Digit(0), 0)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            first_Digit(123.45)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            first_Digit('123')

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            first_Digit()
