import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):
    def test_nonagonal_numbers(self):
        self.assertTrue(is_nonagonal(1))
        self.assertTrue(is_nonagonal(7))
        self.assertTrue(is_nonagonal(14))
        self.assertTrue(is_nonagonal(22))
        self.assertTrue(is_nonagonal(31))

    def test_non_nonagonal_numbers(self):
        self.assertFalse(is_nonagonal(0))
        self.assertFalse(is_nonagonal(2))
        self.assertFalse(is_nonagonal(3))
        self.assertFalse(is_nonagonal(4))
        self.assertFalse(is_nonagonal(5))

    def test_edge_cases(self):
        self.assertTrue(is_nonagonal(7))
        self.assertFalse(is_nonagonal(6))
