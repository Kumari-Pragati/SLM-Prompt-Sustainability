import unittest
from mbpp_803_code import is_Perfect_Square

class TestIsPerfectSquare(unittest.TestCase):
    def test_simple_perfect_square(self):
        self.assertTrue(is_Perfect_Square(4))
        self.assertTrue(is_Perfect_Square(9))
        self.assertTrue(is_Perfect_Square(25))

    def test_non_perfect_square(self):
        self.assertFalse(is_Perfect_Square(3))
        self.assertFalse(is_Perfect_Square(5))
        self.assertFalse(is_Perfect_Square(6))
        self.assertFalse(is_Perfect_Square(7))
        self.assertFalse(is_Perfect_Square(10))

    def test_edge_cases(self):
        self.assertTrue(is_Perfect_Square(0))
        self.assertTrue(is_Perfect_Square(1))
        self.assertFalse(is_Perfect_Square(2))
        self.assertTrue(is_Perfect_Square(16))
        self.assertTrue(is_Perfect_Square(26))
