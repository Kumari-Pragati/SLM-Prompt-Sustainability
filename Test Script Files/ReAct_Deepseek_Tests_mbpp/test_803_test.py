import unittest
from mbpp_803_code import is_Perfect_Square

class TestIsPerfectSquare(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_Perfect_Square(1))
        self.assertTrue(is_Perfect_Square(4))
        self.assertTrue(is_Perfect_Square(9))
        self.assertTrue(is_Perfect_Square(16))
        self.assertTrue(is_Perfect_Square(25))

    def test_edge_cases(self):
        self.assertFalse(is_Perfect_Square(0))
        self.assertFalse(is_Perfect_Square(-1))
        self.assertFalse(is_Perfect_Square(2))
        self.assertFalse(is_Perfect_Square(3))
        self.assertFalse(is_Perfect_Square(5))
        self.assertFalse(is_Perfect_Square(7))
        self.assertFalse(is_Perfect_Square(8))
        self.assertFalse(is_Perfect_Square(17))
        self.assertFalse(is_Perfect_Square(10000))

    def test_large_numbers(self):
        self.assertTrue(is_Perfect_Square(803**2))
        self.assertFalse(is_Perfect_Square(804**2))
