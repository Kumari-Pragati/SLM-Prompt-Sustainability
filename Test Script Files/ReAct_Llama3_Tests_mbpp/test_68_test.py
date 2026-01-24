import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):
    def test_increasing(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))

    def test_decreasing(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))

    def test_constant(self):
        self.assertTrue(is_Monotonic([1, 1, 1, 1, 1]))

    def test_mixed(self):
        self.assertFalse(is_Monotonic([1, 2, 3, 2, 1]))

    def test_single_element(self):
        self.assertTrue(is_Monotonic([1]))

    def test_empty(self):
        self.assertTrue(is_Monotonic([]))

    def test_single_element_decreasing(self):
        self.assertTrue(is_Monotonic([5]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_Monotonic('not a list')
