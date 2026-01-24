import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):

    def test_simple_abundant(self):
        self.assertTrue(is_abundant(12))
        self.assertTrue(is_abundant(28))

    def test_simple_not_abundant(self):
        self.assertFalse(is_abundant(11))
        self.assertFalse(is_abundant(27))

    def test_edge_cases(self):
        self.assertTrue(is_abundant(2))
        self.assertTrue(is_abundant(120))
        self.assertFalse(is_abundant(1))
        self.assertFalse(is_abundant(121))
