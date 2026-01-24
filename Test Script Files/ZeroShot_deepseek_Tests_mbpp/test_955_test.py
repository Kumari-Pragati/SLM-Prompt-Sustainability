import unittest
from mbpp_955_code import is_abundant

class TestAbundantNumber(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(is_abundant(12))
        self.assertTrue(is_abundant(18))
        self.assertTrue(is_abundant(20))

    def test_negative_numbers(self):
        self.assertFalse(is_abundant(8))
        self.assertFalse(is_abundant(10))
        self.assertFalse(is_abundant(15))

    def test_edge_cases(self):
        self.assertFalse(is_abundant(0))
        self.assertFalse(is_abundant(1))
        self.assertFalse(is_abundant(2))
