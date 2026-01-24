import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    def test_single_digit_number(self):
        self.assertEqual(first_Digit(5), 5)

    def test_double_digit_number(self):
        self.assertEqual(first_Digit(23), 2)

    def test_large_number(self):
        self.assertEqual(first_Digit(123456789), 1)

    def test_negative_number(self):
        self.assertEqual(first_Digit(-123), -1)

    def test_zero(self):
        self.assertEqual(first_Digit(0), 0)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            first_Digit(12.34)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            first_Digit("123")
