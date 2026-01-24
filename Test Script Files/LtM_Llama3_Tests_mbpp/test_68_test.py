import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):
    def test_simple_increasing(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))

    def test_simple_decreasing(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))

    def test_empty_input(self):
        self.assertFalse(is_Monotonic([]))

    def test_single_element_input(self):
        self.assertTrue(is_Monotonic([1]))

    def test_all_equal_input(self):
        self.assertTrue(is_Monotonic([1, 1, 1, 1, 1]))

    def test_mixed_increasing_and_decreasing(self):
        self.assertFalse(is_Monotonic([1, 2, 3, 4, 3, 2, 1]))

    def test_increasing_and_decreasing_subsequences(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5, 4, 3, 2, 1]))
