import unittest
from706_code import is_subset

class TestIsSubset(unittest.TestCase):
    def test_empty_arrays(self):
        self.assertTrue(is_subset([], 0, [], 0))

    def test_single_element_arrays(self):
        self.assertTrue(is_subset([1], 1, [], 0))
        self.assertFalse(is_subset([], 0, [1], 1))

    def test_identical_arrays(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2, 3], 3))

    def test_one_subset_of_another(self):
        self.assertTrue(is_subset([1, 2], 2, [1, 2, 3], 3))

    def test_one_array_larger_than_another(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2], 2))

    def test_one_array_smaller_than_another(self):
        self.assertFalse(is_subset([1, 2], 2, [1, 2, 3], 3))

    def test_arrays_with_duplicates(self):
        self.assertTrue(is_subset([1, 1, 2], 3, [1, 2], 2))

    def test_arrays_with_negative_numbers(self):
        self.assertTrue(is_subset([-1, 2], 2, [2, -1], 2))

    def test_arrays_with_floats(self):
        self.assertTrue(is_subset([1.0, 2.0], 2, [1, 2], 2))

    def test_arrays_with_non_numeric_elements(self):
        self.assertRaises(TypeError, is_subset, ['a', 'b'], 2, [1, 2], 2)
