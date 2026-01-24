import unittest
from mbpp_803_code import is_Perfect_Square

class TestPerfectSquare(unittest.TestCase):

    def test_perfect_square(self):
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

    def test_not_perfect_square(self):
        self.assertFalse(is_Perfect_Square(2))
        self.assertFalse(is_Perfect_Square(8))
        self.assertFalse(is_Perfect_Square(18))
        self.assertFalse(is_Perfect_Square(32))
        self.assertFalse(is_Perfect_Square(50))
        self.assertFalse(is_Perfect_Square(63))
        self.assertFalse(is_Perfect_Square(72))
        self.assertFalse(is_Perfect_Square(98))
        self.assertFalse(is_Perfect_Square(101))
        self.assertFalse(is_Perfect_Square(121))
