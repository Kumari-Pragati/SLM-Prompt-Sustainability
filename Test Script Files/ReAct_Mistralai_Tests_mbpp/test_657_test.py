import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_positive_numbers(self):
        """Test positive integers"""
        self.assertEqual(first_Digit(12), 1)
        self.assertEqual(first_Digit(98), 9)
        self.assertEqual(first_Digit(1024), 1)
        self.assertEqual(first_Digit(999999), 9)

    def test_zero(self):
        """Test zero"""
        self.assertEqual(first_Digit(0), 0)

    def test_negative_numbers(self):
        """Test negative integers"""
        self.assertEqual(first_Digit(-1), 0)
        self.assertEqual(first_Digit(-123), 3)
        self.assertEqual(first_Digit(-1000), 0)

    def test_fractional_numbers(self):
        """Test non-integer numbers"""
        self.assertEqual(first_Digit(3.14), 3)
        self.assertEqual(first_Digit(2.00001), 2)
        self.assertEqual(first_Digit(-3.14), 3)

    def test_large_numbers(self):
        """Test very large numbers"""
        self.assertEqual(first_Digit(10**100), 0)

    def test_error_handling(self):
        """Test exceptions"""
        with self.assertRaises(TypeError):
            first_Digit(None)
        with self.assertRaises(TypeError):
            first_Digit([])
        with self.assertRaises(TypeError):
            first_Digit("str")
