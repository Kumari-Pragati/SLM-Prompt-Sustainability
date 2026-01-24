import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(last_Digit(123), 3)

    def test_negative_number(self):
        self.assertEqual(last_Digit(-123), 3)

    def test_zero(self):
        self.assertEqual(last_Digit(0), 0)

    def test_single_digit_number(self):
        self.assertEqual(last_Digit(5), 5)

    def test_large_number(self):
        self.assertEqual(last_Digit(123456789), 9)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            last_Digit('123')
