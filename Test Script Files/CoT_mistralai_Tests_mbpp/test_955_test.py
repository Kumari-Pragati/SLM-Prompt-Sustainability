import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):

    def test_is_abundant_positive(self):
        self.assertTrue(is_abundant(12))
        self.assertTrue(is_abundant(28))
        self.assertTrue(is_abundant(75))

    def test_is_abundant_negative(self):
        self.assertFalse(is_abundant(23))
        self.assertFalse(is_abundant(113))
        self.assertFalse(is_abundant(180))

    def test_is_abundant_boundary(self):
        self.assertFalse(is_abundant(1))
        self.assertTrue(is_abundant(120))

    def test_is_abundant_invalid(self):
        self.assertRaises(TypeError, is_abundant, 'not_a_number')
        self.assertRaises(TypeError, is_abundant, -1)
        self.assertRaises(TypeError, is_abundant, float('nan'))
