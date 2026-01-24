import unittest
from mbpp_803_code import is_Perfect_Square

class TestIsPerfectSquare(unittest.TestCase):

    def test_perfect_square(self):
        self.assertTrue(is_Perfect_Square(9))
        self.assertTrue(is_Perfect_Square(16))
        self.assertTrue(is_Perfect_Square(25))

    def test_non_perfect_square(self):
        self.assertFalse(is_Perfect_Square(8))
        self.assertFalse(is_Perfect_Square(15))
        self.assertFalse(is_Perfect_Square(30))

    def test_edge_cases(self):
        self.assertTrue(is_Perfect_Square(0))
        self.assertFalse(is_Perfect_Square(1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_Perfect_Square("a")
