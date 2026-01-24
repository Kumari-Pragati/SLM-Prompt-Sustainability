import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):
    def test_monotonic_increasing(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))
        self.assertTrue(is_Monotonic([0, -1, -2, -3, -4]))

    def test_monotonic_decreasing(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))
        self.assertTrue(is_Monotonic([4, 3, 2, 1, 0]))

    def test_non_monotonic(self):
        self.assertFalse(is_Monotonic([1, 2, 3, 4, 5, 2]))
        self.assertFalse(is_Monotonic([0, 1, 2, 3, 2]))
