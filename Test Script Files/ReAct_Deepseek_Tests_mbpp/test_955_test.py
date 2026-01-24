import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_abundant(12))
        self.assertFalse(is_abundant(6))
        self.assertTrue(is_abundant(18))
        self.assertFalse(is_abundant(28))

    def test_edge_cases(self):
        self.assertFalse(is_abundant(0))
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
        self.assertFalse(is_abundant(11))

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            is_abundant("12")
        with self.assertRaises(TypeError):
            is_abundant(-12)
