import unittest
from mbpp_706_code import is_subset

class TestIsSubset(unittest.TestCase):
    
    def test_typical_case(self):
        arr1 = [11, 1, 13, 21, 3, 7]
        arr2 = [11, 3, 7, 1]
        self.assertTrue(is_subset(arr1, len(arr1), arr2, len(arr2)))

    def test_empty_array(self):
        arr1 = []
        arr2 = [1, 2, 3]
        self.assertTrue(is_subset(arr1, len(arr1), arr2, len(arr2)))

    def test_subset_at_start(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2]
        self.assertTrue(is_subset(arr1, len(arr1), arr2, len(arr2)))

    def test_subset_at_end(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [4, 5]
        self.assertTrue(is_subset(arr1, len(arr1), arr2, len(arr2)))

    def test_subset_in_middle(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [2, 3]
        self.assertTrue(is_subset(arr1, len(arr1), arr2, len(arr2)))

    def test_non_subset(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [6, 7]
        self.assertFalse(is_subset(arr1, len(arr1), arr2, len(arr2)))

    def test_duplicate_elements(self):
        arr1 = [1, 2, 2, 3, 4]
        arr2 = [2, 2]
        self.assertTrue(is_subset(arr1, len(arr1), arr2, len(arr2)))

    def test_single_element(self):
        arr1 = [1]
        arr2 = [1]
        self.assertTrue(is_subset(arr1, len(arr1), arr2, len(arr2)))

    def test_invalid_input(self):
        arr1 = [1, 2, 3]
        arr2 = [1, 'a']
        with self.assertRaises(TypeError):
            is_subset(arr1, len(arr1), arr2, len(arr2))
