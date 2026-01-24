import unittest
from six hundred import is_Even

class TestIsEven(unittest.TestCase):

    def test_simple_even(self):
        self.assertTrue(is_Even(0))
        self.assertTrue(is_Even(2))
        self.assertTrue(is_Even(4))

    def test_simple_odd(self):
        self.assertFalse(is_Even(1))
        self.assertFalse(is_Even(3))
        self.assertFalse(is_Even(5))

    def test_edge_cases(self):
        self.assertFalse(is_Even(-1))
        self.assertTrue(is_Even(2147483646))  # max int
        self.assertTrue(is_Even(2147483648))  # max int + 1
