import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(last_Digit(12345), 5)
        self.assertEqual(last_Digit(98765), 6)

    def test_zero(self):
        self.assertEqual(last_Digit(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(last_Digit(-12345), 5)
        self.assertEqual(last_Digit(-98765), 5)

    def test_large_numbers(self):
        self.assertEqual(last_Digit(123456789), 9)
        self.assertEqual(last_Digit(987654321), 1)

    def test_floats(self):
        self.assertEqual(last_Digit(12345.678), 8)
        self.assertEqual(last_Digit(-12345.678), 8)
