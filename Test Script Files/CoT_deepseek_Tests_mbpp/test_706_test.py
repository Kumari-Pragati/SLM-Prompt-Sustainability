import unittest
from mbpp_706_code import is_subset

class TestIsSubset(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2, 3, 4, 5], 5))

    def test_empty_arrays(self):
        self.assertTrue(is_subset([], 0, [], 0))

    def test_subset_case(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2], 2))

    def test_non_subset_case(self):
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 2, 4], 3))

    def test_duplicate_elements(self):
        self.assertTrue(is_subset([1, 2, 2], 3, [2], 1))

    def test_negative_numbers(self):
        self.assertTrue(is_subset([-1, -2, -3], 3, [-1, -2], 2))

    def test_large_numbers(self):
        self.assertTrue(is_subset(list(range(1, 1001)), 1000, list(range(1, 1001)), 1000))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_subset("not an array", 1, [1, 2, 3], 3)
