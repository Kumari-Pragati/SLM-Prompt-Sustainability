import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):

    def test_typical_abundant(self):
        self.assertTrue(is_abundant(12))
        self.assertTrue(is_abundant(28))
        self.assertTrue(is_abundant(496))

    def test_typical_not_abundant(self):
        self.assertFalse(is_abundant(23))
        self.assertFalse(is_abundant(24))
        self.assertFalse(is_abundant(60))

    def test_edge_cases(self):
        self.assertTrue(is_abundant(1))
        self.assertTrue(is_abundant(2))
        self.assertFalse(is_abundant(3))
        self.assertFalse(is_abundant(4))
        self.assertTrue(is_abundant(5))
        self.assertFalse(is_abundant(6))
        self.assertFalse(is_abundant(7))
        self.assertFalse(is_abundant(8))
        self.assertTrue(is_abundant(9))
        self.assertFalse(is_abundant(10))
        self.assertTrue(is_abundant(11))
        self.assertFalse(is_abundant(120))
        self.assertFalse(is_abundant(121))
        self.assertTrue(is_abundant(122))
