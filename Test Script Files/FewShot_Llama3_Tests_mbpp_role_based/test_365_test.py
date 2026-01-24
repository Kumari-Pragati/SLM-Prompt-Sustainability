import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(count_Digit(123), 3)

    def test_zero(self):
        self.assertEqual(count_Digit(0), 1)

    def test_negative_integer(self):
        self.assertEqual(count_Digit(-123), 3)

    def test_single_digit(self):
        self.assertEqual(count_Digit(9), 1)

    def test_zero_digit(self):
        self.assertEqual(count_Digit(0), 1)

    def test_large_integer(self):
        self.assertEqual(count_Digit(123456789), 9)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Digit("abc")
