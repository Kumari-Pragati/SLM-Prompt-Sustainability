import unittest
from mbpp_803_code import is_Perfect_Square

class TestIsPerfectSquare(unittest.TestCase):
    
    def test_typical_cases(self):
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
        self.assertFalse(is_Perfect_Square(-1))
        self.assertFalse(is_Perfect_Square(-100))
        self.assertFalse(is_Perfect_Square(2))
        self.assertFalse(is_Perfect_Square(17))
        self.assertFalse(is_Perfect_Square(101))
        self.assertFalse(is_Perfect_Square(1000))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Perfect_Square('a')
        with self.assertRaises(TypeError):
            is_Perfect_Square(None)
        with self.assertRaises(TypeError):
            is_Perfect_Square([1,2,3])
        with self.assertRaises(TypeError):
            is_Perfect_Square({'a': 1, 'b': 2})
