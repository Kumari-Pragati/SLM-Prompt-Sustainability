import unittest
from mbpp_600_code import divmod

class TestIsEven(unittest.TestCase):

    def test_normal_even_numbers(self):
        self.assertTrue(is_Even(0))
        self.assertTrue(is_Even(2))
        self.assertTrue(is_Even(4))
        self.assertTrue(is_Even(6))
        self.assertTrue(is_Even(8))

    def test_normal_odd_numbers(self):
        self.assertFalse(is_Even(1))
        self.assertFalse(is_Even(3))
        self.assertFalse(is_Even(5))
        self.assertFalse(is_Even(7))
        self.assertFalse(is_Even(9))

    def test_edge_cases(self):
        self.assertTrue(is_Even(-2))
        self.assertTrue(is_Even(-4))
        self.assertFalse(is_Even(-1))
        self.assertFalse(is_Even(-3))

    def test_boundary_cases(self):
        self.assertTrue(is_Even(1024))
        self.assertTrue(is_Even(-1024))
        self.assertFalse(is_Even(1025))
        self.assertFalse(is_Even(-1025))
