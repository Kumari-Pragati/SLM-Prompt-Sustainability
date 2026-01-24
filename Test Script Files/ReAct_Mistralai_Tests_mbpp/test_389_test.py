import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):

    def test_zero(self):
        """Test finding Lucas number for n=0"""
        self.assertEqual(find_lucas(0), 2)

    def test_one(self):
        """Test finding Lucas number for n=1"""
        self.assertEqual(find_lucas(1), 1)

    def test_positive_small(self):
        """Test finding Lucas number for small positive integers"""
        self.assertEqual(find_lucas(2), 3)
        self.assertEqual(find_lucas(3), 4)
        self.assertEqual(find_lucas(4), 7)

    def test_negative(self):
        """Test handling negative input"""
        self.assertRaises(ValueError, find_lucas, -1)

    def test_large(self):
        """Test finding Lucas number for large positive integers"""
        self.assertEqual(find_lucas(10), 125862426253)
        self.assertEqual(find_lucas(20), 125862426253 * (5 ** 10) - 13)
