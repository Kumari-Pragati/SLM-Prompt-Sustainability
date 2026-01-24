import unittest
from mbpp_302_code import set_Bit_Number

class TestSetBitNumber(unittest.TestCase):

    def test_zero(self):
        """Test setting bit for input 0"""
        self.assertEqual(set_Bit_Number(0), 0)

    def test_positive_integer(self):
        """Test setting bit for positive integers"""
        for i in range(1, 32):
            self.assertEqual(set_Bit_Number(i), (1 << i))

    def test_negative_integer(self):
        """Test setting bit for negative integers"""
        for i in range(-32, 0, -1):
            self.assertEqual(set_Bit_Number(i), set_Bit_Number(-i))

    def test_large_integer(self):
        """Test setting bit for large integers"""
        self.assertEqual(set_Bit_Number(2**31), (1 << 31))
        self.assertEqual(set_Bit_Number(2**32), 0)

    def test_float(self):
        """Test setting bit for float values"""
        with self.assertRaises(TypeError):
            set_Bit_Number(3.14)

    def test_string(self):
        """Test setting bit for string values"""
        with self.assertRaises(TypeError):
            set_Bit_Number("Hello")
