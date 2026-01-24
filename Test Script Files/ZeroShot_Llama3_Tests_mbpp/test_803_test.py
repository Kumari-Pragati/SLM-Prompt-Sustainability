import unittest
from mbpp_803_code import is_Perfect_Square

class TestIsPerfectSquare(unittest.TestCase):

    def test_perfect_square(self):
        self.assertTrue(is_Perfect_Square(16))
        self.assertTrue(is_Perfect_Square(25))
        self.assertTrue(is_Perfect_Square(36))
        self.assertTrue(is_Perfect_Square(49))
        self.assertTrue(is_Perfect_Square(64))
        self.assertTrue(is_Perfect_Square(81))
        self.assertTrue(is_Perfect_Square(100))

    def test_non_perfect_square(self):
        self.assertFalse(is_Perfect_Square(2))
        self.assertFalse(is_Perfect_Square(3))
        self.assertFalse(is_Perfect_Square(5))
        self.assertFalse(is_Perfect_Square(7))
        self.assertFalse(is_Perfect_Square(11))
        self.assertFalse(is_Perfect_Square(13))

    def test_edge_cases(self):
        self.assertFalse(is_Perfect_Square(0))
        self.assertFalse(is_Perfect_Square(1))
