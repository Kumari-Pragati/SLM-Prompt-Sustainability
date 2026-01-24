import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):
    def test_increasing_sequence(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))

    def test_decreasing_sequence(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))

    def test_constant_sequence(self):
        self.assertTrue(is_Monotonic([1, 1, 1, 1, 1]))

    def test_mixed_sequence(self):
        self.assertFalse(is_Monotonic([1, 2, 3, 3, 4]))

    def test_empty_sequence(self):
        self.assertTrue(is_Monotonic([]))

    def test_single_element_sequence(self):
        self.assertTrue(is_Monotonic([1]))
