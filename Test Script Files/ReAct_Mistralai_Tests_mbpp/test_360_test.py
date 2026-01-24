import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):

    def test_get_carol_positive_integer(self):
        """Test get_carol with positive integer"""
        for n in range(1, 6):
            result = get_carol(n)
            self.assertEqual(result, (2**n) - 1)

    def test_get_carol_zero(self):
        """Test get_carol with zero"""
        result = get_carol(0)
        self.assertEqual(result, -2)

    def test_get_carol_negative_integer(self):
        """Test get_carol with negative integer"""
        for n in range(-1, 0):
            result = get_carol(n)
            self.assertEqual(result, -((2**(-n)) - 1))

    def test_get_carol_large_integer(self):
        """Test get_carol with large integer"""
        result = get_carol(100)
        self.assertEqual(result, (2**100) - 1)

    def test_get_carol_non_integer(self):
        """Test get_carol with non-integer"""
        with self.assertRaises(TypeError):
            get_carol('string')
