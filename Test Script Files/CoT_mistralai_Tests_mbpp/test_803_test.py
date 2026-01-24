import unittest
from mbpp_803_code import is_Perfect_Square

class TestIsPerfectSquare(unittest.TestCase):
    def test_perfect_square(self):
        self.assertTrue(is_Perfect_Square(4))
        self.assertTrue(is_Perfect_Square(9))
        self.assertTrue(is_Perfect_Square(25))
        self.assertTrue(is_Perfect_Square(49))
        self.assertTrue(is_Perfect_Square(169))

    def test_non_perfect_square(self):
        self.assertFalse(is_Perfect_Square(5))
        self.assertFalse(is_Perfect_Square(6))
        self.assertFalse(is_Perfect_Square(7))
        self.assertFalse(is_Perfect_Square(8))
        self.assertFalse(is_Perfect_Square(10))
        self.assertFalse(is_Perfect_Square(121))

    def test_zero(self):
        self.assertFalse(is_Perfect_Square(0))

    def test_negative_numbers(self):
        self.assertFalse(is_Perfect_Square(-1))
        self.assertFalse(is_Perfect_Square(-4))
        self.assertFalse(is_Perfect_Square(-9))
