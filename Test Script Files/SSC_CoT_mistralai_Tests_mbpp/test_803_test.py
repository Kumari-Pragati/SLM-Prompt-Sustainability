import unittest
from mbpp_803_code import is_Perfect_Square

class TestIsPerfectSquare(unittest.TestCase):

    def test_perfect_square(self):
        self.assertTrue(is_Perfect_Square(4))
        self.assertTrue(is_Perfect_Square(9))
        self.assertTrue(is_Perfect_Square(25))
        self.assertTrue(is_Perfect_Square(49))

    def test_edge_cases(self):
        self.assertFalse(is_Perfect_Square(0))
        self.assertFalse(is_Perfect_Square(1))
        self.assertFalse(is_Perfect_Square(2))
        self.assertTrue(is_Perfect_Square(3))
        self.assertFalse(is_Perfect_Square(5))
        self.assertFalse(is_Perfect_Square(6))
        self.assertFalse(is_Perfect_Square(7))
        self.assertFalse(is_Perfect_Square(8))
        self.assertTrue(is_Perfect_Square(16))
        self.assertFalse(is_Perfect_Square(17))
        self.assertTrue(is_Perfect_Square(20))
        self.assertFalse(is_Perfect_Square(21))
        self.assertTrue(is_Perfect_Square(28))
        self.assertFalse(is_Perfect_Square(29))
        self.assertTrue(is_Perfect_Square(36))
        self.assertFalse(is_Perfect_Square(37))
        self.assertTrue(is_Perfect_Square(44))
        self.assertFalse(is_Perfect_Square(45))
        self.assertTrue(is_Perfect_Square(625))
