import unittest
from mbpp_467_code import decimal_to_Octal

class TestDecimalToOctal(unittest.TestCase):

    def test_zero(self):
        """Test converting zero to octal"""
        self.assertEqual(decimal_to_Octal(0), '0')

    def test_positive_small(self):
        """Test converting small positive numbers to octal"""
        self.assertEqual(decimal_to_Octal(7), '111')
        self.assertEqual(decimal_to_Octal(10), '12')
        self.assertEqual(decimal_to_Octal(15), '17' )

    def test_positive_large(self):
        """Test converting large positive numbers to octal"""
        self.assertEqual(decimal_to_Octal(100), '144')
        self.assertEqual(decimal_to_Octal(255), '377')
        self.assertEqual(decimal_to_Octal(1000), '1331')

    def test_negative_small(self):
        """Test converting small negative numbers to octal"""
        self.assertEqual(decimal_to_Octal(-7), '377')
        self.assertEqual(decimal_to_Octal(-10), '1777')
        self.assertEqual(decimal_to_Octal(-15), '3777')

    def test_negative_large(self):
        """Test converting large negative numbers to octal"""
        self.assertEqual(decimal_to_Octal(-100), '2000')
        self.assertEqual(decimal_to_Octal(-255), '777')
        self.assertEqual(decimal_to_Octal(-1000), '37777')

    def test_overflow(self):
        """Test handling of overflow (numbers larger than 37777777777)"""
        self.assertEqual(decimal_to_Octal(38), '10010')
        self.assertEqual(decimal_to_Octal(380), '1001000')
        self.assertEqual(decimal_to_Octal(3800), '10010000')
        self.assertEqual(decimal_to_Octal(38000), '100100000')
        self.assertEqual(decimal_to_Octal(380000), '1001000000')
        self.assertEqual(decimal_to_Octal(3800000), '10010000000')
        self.assertEqual(decimal_to_Octal(38000000), '100100000000')
        self.assertEqual(decimal_to_Octal(380000000), '1001000000000')
        self.assertEqual(decimal_to_Octal(3800000000), '10010000000000')
