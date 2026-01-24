import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))
        self.assertTrue(is_Monotonic([1, 1, 1, 1, 1]))

    def test_edge_conditions(self):
        self.assertTrue(is_Monotonic([]))
        self.assertTrue(is_Monotonic([1]))
        self.assertTrue(is_Monotonic([1, 2]))
        self.assertTrue(is_Monotonic([2, 1]))

    def test_boundary_conditions(self):
        self.assertTrue(is_Monotonic([-1, 0, 1]))
        self.assertTrue(is_Monotonic([0, -1, 1]))
        self.assertTrue(is_Monotonic([-1, -2, -3]))
        self.assertTrue(is_Monotonic([1, 2, 3]))

    def test_complex_cases(self):
        self.assertFalse(is_Monotonic([1, 3, 2]))
        self.assertFalse(is_Monotonic([0, 0, 0, -1]))
        self.assertFalse(is_Monotonic([2, 2, 2, 1]))
