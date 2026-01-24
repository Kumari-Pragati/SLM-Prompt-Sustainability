import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):

    def test_monotonic_increasing(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))
        self.assertTrue(is_Monotonic([1, 1, 1, 1, 1]))
        self.assertTrue(is_Monotonic([10, 11, 12, 13, 14]))

    def test_monotonic_decreasing(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))
        self.assertTrue(is_Monotonic([10, 9, 8, 7, 6]))
        self.assertTrue(is_Monotonic([1, 1, 1, 1, -1]))

    def test_mixed_monotonic(self):
        self.assertFalse(is_Monotonic([1, 2, 3, 4, 5, 6, 7, 6, 5]))
        self.assertFalse(is_Monotonic([1, 2, 3, 2, 1]))
        self.assertFalse(is_Monotonic([5, 4, 3, 2, 1, 2, 3, 4, 5]))

    def test_empty_list(self):
        self.assertTrue(is_Monotonic([]))

    def test_single_element(self):
        self.assertTrue(is_Monotonic([1]))
