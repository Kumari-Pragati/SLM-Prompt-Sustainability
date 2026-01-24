import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):

    def test_perfect_square(self):
        """Test perfect square"""
        self.assertEqual(next_Perfect_Square(4), 9)
        self.assertEqual(next_Perfect_Square(16), 25)
        self.assertEqual(next_Perfect_Square(25), 36)
        self.assertEqual(next_Perfect_Square(36), 49)
        self.assertEqual(next_Perfect_Square(625), 649)

    def test_non_perfect_square(self):
        """Test non-perfect square"""
        self.assertNotEqual(next_Perfect_Square(3), 9)
        self.assertNotEqual(next_Perfect_Square(5), 25)
        self.assertNotEqual(next_Perfect_Square(7), 49)
        self.assertNotEqual(next_Perfect_Square(8), 49)  # Edge case: 2^3 is a perfect square
        self.assertNotEqual(next_Perfect_Square(9), 49)  # Edge case: 3^2 is a perfect square

    def test_zero(self):
        """Test with zero"""
        self.assertRaises(ValueError, next_Perfect_Square, 0)

    def test_negative(self):
        """Test with negative numbers"""
        self.assertRaises(ValueError, next_Perfect_Square, -1)
        self.assertRaises(ValueError, next_Perfect_Square, -4)
        self.assertRaises(ValueError, next_Perfect_Square, -25)
