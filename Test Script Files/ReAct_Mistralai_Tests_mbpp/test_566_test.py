import unittest
from mbpp_566_code import sum_digits

class TestSumDigits(unittest.TestCase):

    def test_zero(self):
        """Test sum_digits(0) returns 0"""
        self.assertEqual(sum_digits(0), 0)

    def test_positive_small(self):
        """Test sum_digits(small positive numbers)"""
        self.assertEqual(sum_digits(12), 3)
        self.assertEqual(sum_digits(98), 17)

    def test_positive_large(self):
        """Test sum_digits(large positive numbers)"""
        self.assertEqual(sum_digits(123456), 35)
        self.assertEqual(sum_digits(9876543), 45)

    def test_negative_small(self):
        """Test sum_digits(small negative numbers)"""
        self.assertEqual(sum_digits(-12), 3)
        self.assertEqual(sum_digits(-98), 17)

    def test_negative_large(self):
        """Test sum_digits(large negative numbers)"""
        self.assertEqual(sum_digits(-123456), 35)
        self.assertEqual(sum_digits(-9876543), 45)

    def test_float(self):
        """Test sum_digits(float)"""
        self.assertEqual(sum_digits(12.34), 6)
        self.assertEqual(sum_digits(-12.34), 6)

    def test_large_float(self):
        """Test sum_digits(large float)"""
        self.assertEqual(sum_digits(123456.78), 34)
        self.assertEqual(sum_digits(-123456.78), 34)

    def test_large_positive(self):
        """Test sum_digits(very large positive number)"""
        self.assertEqual(sum_digits(1234567890), 45)

    def test_large_negative(self):
        """Test sum_digits(very large negative number)"""
        self.assertEqual(sum_digits(-1234567890), 45)
