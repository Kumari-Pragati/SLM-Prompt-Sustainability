import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):
    def test_abundant_numbers(self):
        self.assertTrue(is_abundant(12))
        self.assertTrue(is_abundant(24))
        self.assertTrue(is_abundant(36))

    def test_non_abundant_numbers(self):
        self.assertFalse(is_abundant(1))
        self.assertFalse(is_abundant(2))
        self.assertFalse(is_abundant(3))
        self.assertFalse(is_abundant(4))
        self.assertFalse(is_abundant(5))
        self.assertFalse(is_abundant(6))
        self.assertFalse(is_abundant(7))
        self.assertFalse(is_abundant(8))
        self.assertFalse(is_abundant(9))
        self.assertFalse(is_abundant(10))

    def test_edge_cases(self):
        self.assertFalse(is_abundant(11))
        self.assertFalse(is_abundant(13))
        self.assertFalse(is_abundant(14))
        self.assertFalse(is_abundant(15))
        self.assertFalse(is_abundant(16))
        self.assertFalse(is_abundant(17))
        self.assertFalse(is_abundant(18))
        self.assertFalse(is_abundant(19))
        self.assertFalse(is_abundant(20))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_abundant('a')
        with self.assertRaises(TypeError):
            is_abundant(None)
