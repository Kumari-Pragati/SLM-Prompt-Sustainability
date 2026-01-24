import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))
        self.assertTrue(is_Monotonic([1, 1, 1, 1, 1]))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(is_Monotonic([1]))
        self.assertTrue(is_Monotonic([]))

    def test_corner_cases(self):
        self.assertFalse(is_Monotonic([2, 1]))
        self.assertTrue(is_Monotonic([1, 2]))
        self.assertTrue(is_Monotonic([1, 2, 2, 3]))
        self.assertFalse(is_Monotonic([3, 2, 2, 1]))
