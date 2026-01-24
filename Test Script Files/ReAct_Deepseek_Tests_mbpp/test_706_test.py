import unittest
from mbpp_706_code import is_subset

class TestIsSubset(unittest.TestCase):

    def test_typical_case(self):
        arr1 = [11, 1, 13, 21, 3, 7]
        arr2 = [11, 3, 7, 1]
        self.assertTrue(is_subset(arr1, len(arr1), arr2, len(arr2)))

    def test_empty_arrays(self):
        arr1 = []
        arr2 = []
        self.assertTrue(is_subset(arr1, len(arr1), arr2, len(arr2)))

    def test_subset_with_duplicates(self):
        arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        arr2 = [1, 2, 2, 3, 3, 4, 4, 5, 5]
        self.assertTrue(is_subset(arr1, len(arr1), arr2, len(arr2)))

    def test_non_subset(self):
        arr1 = [1, 2, 3, 4, 5, 6]
        arr2 = [1, 2, 3, 4, 5, 7]
        self.assertFalse(is_subset(arr1, len(arr1), arr2, len(arr2)))

    def test_large_arrays(self):
        arr1 = list(range(1, 1001))
        arr2 = list(range(1, 1000))
        self.assertFalse(is_subset(arr1, len(arr1), arr2, len(arr2)))
