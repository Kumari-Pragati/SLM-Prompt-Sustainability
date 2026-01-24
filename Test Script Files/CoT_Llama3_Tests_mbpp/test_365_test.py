import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(count_Digit(123), 3)
        self.assertEqual(count_Digit(456), 3)
        self.assertEqual(count_Digit(789), 3)

    def test_zero(self):
        self.assertEqual(count_Digit(0), 1)

    def test_negative_numbers(self):
        self.assertEqual(count_Digit(-123), 3)
        self.assertEqual(count_Digit(-456), 3)
        self.assertEqual(count_Digit(-789), 3)

    def test_single_digit_numbers(self):
        self.assertEqual(count_Digit(1), 1)
        self.assertEqual(count_Digit(2), 1)
        self.assertEqual(count_Digit(3), 1)

    def test_large_numbers(self):
        self.assertEqual(count_Digit(123456789), 9)
        self.assertEqual(count_Digit(987654321), 9)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            count_Digit('123')
        with self.assertRaises(TypeError):
            count_Digit(123.45)
