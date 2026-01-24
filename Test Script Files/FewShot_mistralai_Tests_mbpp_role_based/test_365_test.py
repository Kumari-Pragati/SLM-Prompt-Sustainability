import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(count_Digit(12345), 5)

    def test_zero(self):
        self.assertEqual(count_Digit(0), 1)

    def test_negative_integer(self):
        self.assertEqual(count_Digit(-12345), 5)

    def test_large_integer(self):
        self.assertEqual(count_Digit(1234567890), 10)

    def test_floating_point(self):
        self.assertEqual(count_Digit(123.45), 3)

    def test_empty_string(self):
        self.assertEqual(count_Digit(''), 0)

    def test_string_with_digits(self):
        self.assertEqual(count_Digit('12345'), 5)

    def test_string_with_non_digits(self):
        self.assertEqual(count_Digit('123a5'), 3)
