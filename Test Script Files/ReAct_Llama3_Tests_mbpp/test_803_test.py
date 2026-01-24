import unittest
from mbpp_803_code import is_Perfect_Square

class TestIsPerfectSquare(unittest.TestCase):

    def test_perfect_square(self):
        self.assertTrue(is_Perfect_Square(16))

    def test_non_perfect_square(self):
        self.assertFalse(is_Perfect_Square(17))

    def test_edge_case_zero(self):
        self.assertTrue(is_Perfect_Square(0))

    def test_edge_case_one(self):
        self.assertTrue(is_Perfect_Square(1))

    def test_edge_case_negative(self):
        self.assertFalse(is_Perfect_Square(-1))

    def test_edge_case_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            is_Perfect_Square(0)
