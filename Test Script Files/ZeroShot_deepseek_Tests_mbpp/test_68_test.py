import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(is_Monotonic([]))

    def test_single_element_list(self):
        self.assertTrue(is_Monotonic([1]))

    def test_increasing_list(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))

    def test_decreasing_list(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))

    def test_constant_list(self):
        self.assertTrue(is_Monotonic([1, 1, 1, 1, 1]))

    def test_increasing_decreasing_list(self):
        self.assertFalse(is_Monotonic([1, 2, 3, 2, 1]))

    def test_decreasing_increasing_list(self):
        self.assertFalse(is_Monotonic([5, 4, 3, 4, 5]))

    def test_non_integer_list(self):
        self.assertFalse(is_Monotonic([1, 2.5, 3, 2, 1]))

    def test_non_numeric_list(self):
        with self.assertRaises(TypeError):
            is_Monotonic(['a', 'b', 'c'])
