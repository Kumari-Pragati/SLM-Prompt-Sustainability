import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(first_Digit(12345), 1)
        self.assertEqual(first_Digit(9876), 9)
        self.assertEqual(first_Digit(10), 1)
        self.assertEqual(first_Digit(100), 1)
        self.assertEqual(first_Digit(1000), 1)

    def test_zero(self):
        self.assertEqual(first_Digit(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(first_Digit(-12345), 1)
        self.assertEqual(first_Digit(-9876), 9)
        self.assertEqual(first_Digit(-10), 1)
        self.assertEqual(first_Digit(-100), 1)
        self.assertEqual(first_Digit(-1000), 1)
