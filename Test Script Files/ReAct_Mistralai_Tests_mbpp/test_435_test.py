import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):

    def test_positive_numbers(self):
        """Test positive numbers"""
        self.assertEqual(last_Digit(12345), 5)
        self.assertEqual(last_Digit(9876), 6)

    def test_zero(self):
        """Test zero"""
        self.assertEqual(last_Digit(0), 0)

    def test_negative_numbers(self):
        """Test negative numbers"""
        self.assertEqual(last_Digit(-12345), 5)
        self.assertEqual(last_Digit(-9876), 6)

    def test_large_numbers(self):
        """Test large numbers"""
        self.assertEqual(last_Digit(123456789), 9)
        self.assertEqual(last_Digit(987654321), 1)

    def test_floats(self):
        """Test floats"""
        self.assertEqual(last_Digit(1234.5678), 8)
        self.assertEqual(last_Digit(-9876.5432), 2)
