import unittest
from mbpp_354_code import tn_ap

class TestTnAp(unittest.TestCase):

    def test_positive_numbers(self):
        """Test tn_ap with positive numbers"""
        self.assertEqual(tn_ap(1, 3, 2), 7)
        self.assertEqual(tn_ap(5, 2, 3), 13)
        self.assertEqual(tn_ap(10, 4, 5), 59)

    def test_zero_n(self):
        """Test tn_ap with n=0"""
        self.assertEqual(tn_ap(3, 0, 4), 3)

    def test_negative_numbers(self):
        """Test tn_ap with negative numbers"""
        self.assertEqual(tn_ap(-2, 3, 1), -5)
        self.assertEqual(tn_ap(-5, 2, -3), 11)
        self.assertEqual(tn_ap(-10, 4, -5), -49)

    def test_negative_d(self):
        """Test tn_ap with negative d"""
        self.assertEqual(tn_ap(3, 3, -2), -7)
        self.assertEqual(tn_ap(-5, 2, -3), 11)
        self.assertEqual(tn_ap(-10, 4, -5), -49)

    def test_zero_a(self):
        """Test tn_ap with zero a"""
        self.assertEqual(tn_ap(0, 3, 2), 0)

    def test_zero_d(self):
        """Test tn_ap with zero d"""
        self.assertEqual(tn_ap(3, 3, 0), 9)

    def test_negative_values(self):
        """Test tn_ap with negative values"""
        with self.assertRaises(ValueError):
            tn_ap(-1, 3, -1)  # Negative a and d
        with self.assertRaises(ValueError):
            tn_ap(1, -3, -1)  # Negative n
        with self.assertRaises(ValueError):
            tn_ap(1, 3, 0)  # Zero d
