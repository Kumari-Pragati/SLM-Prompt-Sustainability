import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(first_Digit(12345), 1)
        self.assertEqual(first_Digit(98765), 9)

    def test_zero(self):
        self.assertEqual(first_Digit(0), 0)

    def test_negative_integer(self):
        self.assertEqual(first_Digit(-12345), 1)
        self.assertEqual(first_Digit(-98765), 9)

    def test_single_digit(self):
        for n in range(1, 10):
            self.assertEqual(first_Digit(n), n)

    def test_large_integer(self):
        self.assertEqual(first_Digit(123456789), 1)

    def test_floating_point(self):
        self.assertEqual(first_Digit(123.45), 1)
        self.assertEqual(first_Digit(-123.45), 1)
