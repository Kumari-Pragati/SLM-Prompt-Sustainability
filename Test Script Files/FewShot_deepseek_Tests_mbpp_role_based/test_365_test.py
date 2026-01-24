import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Digit(12345), 5)

    def test_single_digit_number(self):
        self.assertEqual(count_Digit(0), 1)

    def test_large_number(self):
        self.assertEqual(count_Digit(1234567890), 10)

    def test_negative_number(self):
        self.assertEqual(count_Digit(-12345), 5)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            count_Digit(123.45)

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            count_Digit()
