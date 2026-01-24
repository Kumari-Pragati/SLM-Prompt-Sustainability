import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_positive_integer(self):
        """Test positive integers"""
        self.assertEqual(first_Digit(12345), 1)
        self.assertEqual(first_Digit(9876), 9)
        self.assertEqual(first_Digit(10), 1)

    def test_zero(self):
        """Test zero"""
        self.assertEqual(first_Digit(0), 0)

    def test_negative_integer(self):
        """Test negative integers"""
        self.assertEqual(first_Digit(-12345), 1)
        self.assertEqual(first_Digit(-9876), -9)
        self.assertEqual(first_Digit(-10), -1)

    def test_float(self):
        """Test float numbers"""
        self.assertEqual(first_Digit(3.14159), 3)
        self.assertEqual(first_Digit(-3.14159), -3)

    def test_non_integer(self):
        """Test non-integer values"""
        self.assertEqual(first_Digit('abc'), None)
        self.assertEqual(first_Digit(True), None)
        self.assertEqual(first_Digit(None), None)
