import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):

    def test_normal(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))
        self.assertTrue(is_Monotonic([-1, -2, -3, -4, -5]))
        self.assertTrue(is_Monotonic([1, 1, 1, 1, 1]))
        self.assertTrue(is_Monotonic([-1, -1, -1, -1, -1]))

    def test_edge_and_boundary(self):
        self.assertTrue(is_Monotonic([0, 1, 2, 2, 3]))
        self.assertTrue(is_Monotonic([-1, -1, -2, -2, -3]))
        self.assertTrue(is_Monotonic([1, 2, 2, 2, 3]))
        self.assertTrue(is_Monotonic([-1, -2, -2, -2, -3]))
        self.assertTrue(is_Monotonic([1, 2, 3, 2, 1]))
        self.assertTrue(is_Monotonic([-1, -2, -3, -2, -1]))
        self.assertTrue(is_Monotonic([1, 1, 1, 1, 1, 1]))
        self.assertTrue(is_Monotonic([-1, -1, -1, -1, -1, -1]))

    def test_special_cases(self):
        self.assertFalse(is_Monotonic([1, 2, 3, 4, 5, 4]))
        self.assertFalse(is_Monotonic([-1, -2, -3, -4, -5, -4]))
        self.assertFalse(is_Monotonic([1, 2, 3, 4, 4, 5]))
        self.assertFalse(is_Monotonic([-1, -2, -3, -4, -5, -4]))
        self.assertFalse(is_Monotonic([1, 2, 3, 3, 2, 1]))
        self.assertFalse(is_Monotonic([-1, -2, -3, -3, -2, -1]))
