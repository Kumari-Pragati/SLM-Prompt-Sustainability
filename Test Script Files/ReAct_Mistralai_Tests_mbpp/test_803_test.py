import unittest
from mbpp_803_code import is_Perfect_Square

class TestPerfectSquare(unittest.TestCase):

    def test_perfect_square_positive(self):
        """Test for perfect squares within valid range"""
        self.assertTrue(is_Perfect_Square(4))
        self.assertTrue(is_Perfect_Square(9))
        self.assertTrue(is_Perfect_Square(25))
        self.assertTrue(is_Perfect_Square(36))
        self.assertTrue(is_Perfect_Square(64))

    def test_perfect_square_zero(self):
        """Test for perfect square of zero"""
        self.assertFalse(is_Perfect_Square(0))

    def test_perfect_square_negative(self):
        """Test for perfect squares of negative numbers"""
        self.assertFalse(is_Perfect_Square(-1))
        self.assertFalse(is_Perfect_Square(-4))
        self.assertFalse(is_Perfect_Square(-9))
        self.assertFalse(is_Perfect_Square(-25))

    def test_perfect_square_one(self):
        """Test for perfect square of 1"""
        self.assertFalse(is_Perfect_Square(1))

    def test_perfect_square_edge_cases(self):
        """Test for edge cases like 0, 1, and large numbers"""
        self.assertFalse(is_Perfect_Square(0))
        self.assertFalse(is_Perfect_Square(1))
        self.assertFalse(is_Perfect_Square(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000