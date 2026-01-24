import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):

    def test_is_abundant_positive(self):
        self.assertTrue(is_abundant(12))
        self.assertTrue(is_abundant(28))
        self.assertTrue(is_abundant(496))

    def test_is_abundant_negative(self):
        self.assertFalse(is_abundant(11))
        self.assertFalse(is_abundant(27))
        self.assertFalse(is_abundant(50))

    def test_is_abundant_edge_cases(self):
        self.assertFalse(is_abundant(1))
        self.assertTrue(is_abundant(13))
        self.assertTrue(is_abundant(120))
