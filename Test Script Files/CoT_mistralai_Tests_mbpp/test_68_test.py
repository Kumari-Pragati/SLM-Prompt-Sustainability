import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):

    def test_monotonic_increasing(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))
        self.assertTrue(is_Monotonic([-1, -2, -3, -4, -5]))

    def test_monotonic_decreasing(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))
        self.assertTrue(is_Monotonic([5, 4, 3, 2, -1]))

    def test_single_element(self):
        self.assertTrue(is_Monotonic([1]))
        self.assertTrue(is_Monotonic([-1]))

    def test_empty_list(self):
        self.assertTrue(is_Monotonic([]))

    def test_duplicate_elements(self):
        self.assertTrue(is_Monotonic([1, 1, 2, 2, 3]))
        self.assertTrue(is_Monotonic([-1, -1, -2, -2, -3]))

    def test_edge_cases(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 2]))
        self.assertTrue(is_Monotonic([-1, -2, -3, -2]))
        self.assertTrue(is_Monotonic([1, 2, 2, 3]))
        self.assertTrue(is_Monotonic([-1, -2, -2, -3]))

    def test_invalid_inputs(self):
        self.assertFalse(is_Monotonic([1, 2, 3, 2, 1]))
        self.assertFalse(is_Monotonic([-1, -2, -3, 2]))
