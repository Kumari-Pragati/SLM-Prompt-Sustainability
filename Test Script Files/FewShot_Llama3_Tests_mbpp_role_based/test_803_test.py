import unittest
from mbpp_803_code import is_Perfect_Square

class TestIsPerfectSquare(unittest.TestCase):
    def test_perfect_square(self):
        self.assertTrue(is_Perfect_Square(16))

    def test_perfect_square_edge_case(self):
        self.assertTrue(is_Perfect_Square(1))

    def test_non_perfect_square(self):
        self.assertFalse(is_Perfect_Square(3))

    def test_non_perfect_square_edge_case(self):
        self.assertFalse(is_Perfect_Square(2))

    def test_zero(self):
        self.assertFalse(is_Perfect_Square(0))

    def test_negative_number(self):
        self.assertFalse(is_Perfect_Square(-1))
