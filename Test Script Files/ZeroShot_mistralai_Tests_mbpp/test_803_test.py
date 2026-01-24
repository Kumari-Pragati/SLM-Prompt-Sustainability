import unittest
from mbpp_803_code import is_Perfect_Square

class TestPerfectSquare(unittest.TestCase):

    def test_perfect_square_positive(self):
        self.assertTrue(is_Perfect_Square(4))
        self.assertTrue(is_Perfect_Square(9))
        self.assertTrue(is_Perfect_Square(25))
        self.assertTrue(is_Perfect_Square(49))
        self.assertTrue(is_Perfect_Square(169))

    def test_perfect_square_zero(self):
        self.assertFalse(is_Perfect_Square(0))

    def test_perfect_square_negative(self):
        self.assertFalse(is_Perfect_Square(-1))
        self.assertFalse(is_Perfect_Square(-4))
        self.assertFalse(is_Perfect_Square(-9))
        self.assertFalse(is_Perfect_Square(-25))
        self.assertFalse(is_Perfect_Square(-49))

    def test_perfect_square_non_square(self):
        self.assertFalse(is_Perfect_Square(5))
        self.assertFalse(is_Perfect_Square(6))
        self.assertFalse(is_Perfect_Square(7))
        self.assertFalse(is_Perfect_Square(8))
        self.assertFalse(is_Perfect_Square(10))
