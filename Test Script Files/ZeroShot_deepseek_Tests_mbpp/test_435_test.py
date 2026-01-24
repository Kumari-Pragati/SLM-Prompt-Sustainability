import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(last_Digit(123), 3)
        self.assertEqual(last_Digit(456), 6)
        self.assertEqual(last_Digit(789), 9)

    def test_negative_numbers(self):
        self.assertEqual(last_Digit(-123), 3)
        self.assertEqual(last_Digit(-456), 6)
        self.assertEqual(last_Digit(-789), 9)

    def test_single_digit_numbers(self):
        self.assertEqual(last_Digit(0), 0)
        self.assertEqual(last_Digit(5), 5)
        self.assertEqual(last_Digit(10), 0)

    def test_large_numbers(self):
        self.assertEqual(last_Digit(1234567890), 0)
        self.assertEqual(last_Digit(9876543210), 0)
