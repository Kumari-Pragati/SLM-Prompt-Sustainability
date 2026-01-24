import unittest
from mbpp_93_code import power

class TestPowerFunction(unittest.TestCase):

    def test_base_case(self):
        """Test power function with base case (b=1)"""
        self.assertEqual(power(2, 1), 2)
        self.assertEqual(power(-3, 1), -3)
        self.assertEqual(power(0, 1), 0)

    def test_zero_base(self):
        """Test power function with base as zero"""
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(-3, 0), 1)
        self.assertEqual(power(0, 0), 1)

    def test_negative_base(self):
        """Test power function with negative base"""
        self.assertEqual(power(2, -1), 1/2)
        self.assertEqual(power(-3, -1), -1)
        self.assertEqual(power(0, -1), 0)

    def test_large_exponent(self):
        """Test power function with large exponent"""
        self.assertEqual(power(2, 10), 2**10)
        self.assertEqual(power(-3, 10), (-3)**10)
        self.assertEqual(power(0, 10), 0)

    def test_zero_exponent(self):
        """Test power function with zero exponent"""
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(-3, 0), 1)
        self.assertEqual(power(0, 0), 1)
