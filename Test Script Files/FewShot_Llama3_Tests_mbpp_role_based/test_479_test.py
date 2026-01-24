import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(first_Digit(123), 1)

    def test_single_digit(self):
        self.assertEqual(first_Digit(5), 5)

    def test_zero(self):
        self.assertEqual(first_Digit(0), 0)

    def test_negative_integer(self):
        self.assertEqual(first_Digit(-123), -1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            first_Digit('abc')
