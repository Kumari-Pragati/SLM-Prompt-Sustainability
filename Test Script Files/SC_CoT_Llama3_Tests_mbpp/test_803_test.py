import unittest
from mbpp_803_code import is_Perfect_Square

class TestIsPerfectSquare(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertTrue(is_Perfect_Square(1))
        self.assertTrue(is_Perfect_Square(4))
        self.assertTrue(is_Perfect_Square(9))
        self.assertTrue(is_Perfect_Square(16))
        self.assertTrue(is_Perfect_Square(25))
        self.assertTrue(is_Perfect_Square(36))
        self.assertTrue(is_Perfect_Square(49))
        self.assertTrue(is_Perfect_Square(64))
        self.assertTrue(is_Perfect_Square(81))
        self.assertTrue(is_Perfect_Square(100))

    def test_edge_cases(self):
        self.assertFalse(is_Perfect_Square(0))
        self.assertFalse(is_Perfect_Square(2))
        self.assertFalse(is_Perfect_Square(3))
        self.assertFalse(is_Perfect_Square(5))
        self.assertFalse(is_Perfect_Square(6))
        self.assertFalse(is_Perfect_Square(7))
        self.assertFalse(is_Perfect_Square(8))
        self.assertFalse(is_Perfect_Square(10))

    def test_negative_inputs(self):
        self.assertFalse(is_Perfect_Square(-1))
        self.assertFalse(is_Perfect_Square(-4))
        self.assertFalse(is_Perfect_Square(-9))
        self.assertFalse(is_Perfect_Square(-16))
        self.assertFalse(is_Perfect_Square(-25))
        self.assertFalse(is_Perfect_Square(-36))
        self.assertFalse(is_Perfect_Square(-49))
        self.assertFalse(is_Perfect_Square(-64))
        self.assertFalse(is_Perfect_Square(-81))
        self.assertFalse(is_Perfect_Square(-100))

    def test_non_integer_inputs(self):
        self.assertFalse(is_Perfect_Square(1.0))
        self.assertFalse(is_Perfect_Square(4.0))
        self.assertFalse(is_Perfect_Square(9.0))
        self.assertFalse(is_Perfect_Square(16.0))
        self.assertFalse(is_Perfect_Square(25.0))
        self.assertFalse(is_Perfect_Square(36.0))
        self.assertFalse(is_Perfect_Square(49.0))
        self.assertFalse(is_Perfect_Square(64.0))
        self.assertFalse(is_Perfect_Square(81.0))
        self.assertFalse(is_Perfect_Square(100.0))
