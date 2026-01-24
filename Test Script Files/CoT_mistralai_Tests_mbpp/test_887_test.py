import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(5))
        self.assertTrue(is_odd(7))
        self.assertTrue(is_odd(99))

    def test_zero(self):
        self.assertFalse(is_odd(0))

    def test_negative_numbers(self):
        self.assertFalse(is_odd(-1))
        self.assertFalse(is_odd(-3))
        self.assertFalse(is_odd(-5))
        self.assertFalse(is_odd(-7))
        self.assertFalse(is_odd(-99))

    def test_edge_cases(self):
        self.assertTrue(is_odd(2**32 - 1))
        self.assertFalse(is_odd(2**32))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_odd, 'not_a_number')
        self.assertRaises(TypeError, is_odd, [1, 2, 3])
        self.assertRaises(TypeError, is_odd, (1, 2, 3))
        self.assertRaises(TypeError, is_odd, None)
        self.assertRaises(TypeError, is_odd, True)
        self.assertRaises(TypeError, is_odd, False)
