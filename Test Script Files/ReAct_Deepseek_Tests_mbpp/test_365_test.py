import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(count_Digit(12345), 5)
        self.assertEqual(count_Digit(9876543210), 10)

    def test_zero(self):
        self.assertEqual(count_Digit(0), 1)

    def test_negative_numbers(self):
        self.assertEqual(count_Digit(-12345), 5)
        self.assertEqual(count_Digit(-9876543210), 10)

    def test_single_digit_numbers(self):
        self.assertEqual(count_Digit(5), 1)
        self.assertEqual(count_Digit(0), 1)

    def test_large_numbers(self):
        self.assertEqual(count_Digit(10**1000), 1000)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            count_Digit(123.45)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            count_Digit('12345')
