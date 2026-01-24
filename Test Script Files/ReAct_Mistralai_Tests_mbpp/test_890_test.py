import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):

    def test_find_extra_with_different_elements(self):
        """Test finding the index of the first different element"""
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 6, 5]
        self.assertEqual(find_Extra(arr1, arr2, len(arr1)), 3)

    def test_find_extra_with_same_elements(self):
        """Test when all elements are the same"""
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4, 5]
        self.assertEqual(find_Extra(arr1, arr2, len(arr1)), len(arr1))

    def test_find_extra_with_empty_arrays(self):
        """Test when both arrays are empty"""
        arr1 = []
        arr2 = []
        self.assertEqual(find_Extra(arr1, arr2, len(arr1)), len(arr1))

    def test_find_extra_with_one_element(self):
        """Test when one array has one element and the other is empty"""
        arr1 = [1]
        arr2 = []
        self.assertEqual(find_Extra(arr1, arr2, len(arr1)), 0)

    def test_find_extra_with_negative_index(self):
        """Test when the index is negative"""
        arr1 = [1, 2, 3]
        arr2 = [1, 2, 3]
        with self.assertRaises(IndexError):
            find_Extra(arr1, arr2, -1)

    def test_find_extra_with_out_of_range_index(self):
        """Test when the index is out of range"""
        arr1 = [1, 2, 3]
        arr2 = [1, 2, 3]
        with self.assertRaises(IndexError):
            find_Extra(arr1, arr2, len(arr1) + 1)
