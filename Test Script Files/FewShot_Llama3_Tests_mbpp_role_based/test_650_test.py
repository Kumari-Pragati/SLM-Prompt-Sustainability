import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):
    def test_equal_arrays(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4, 5]
        self.assertTrue(are_Equal(arr1, arr2, 5, 5))

    def test_non_equal_arrays(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 5, 6]
        self.assertFalse(are_Equal(arr1, arr2, 5, 5))

    def test_arrays_of_different_lengths(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4]
        self.assertFalse(are_Equal(arr1, arr2, 5, 4))

    def test_arrays_with_duplicates(self):
        arr1 = [1, 2, 2, 3, 4, 5]
        arr2 = [1, 2, 2, 3, 4, 5]
        self.assertTrue(are_Equal(arr1, arr2, 6, 6))

    def test_arrays_with_negative_numbers(self):
        arr1 = [-1, -2, -3, -4, -5]
        arr2 = [-1, -2, -3, -4, -5]
        self.assertTrue(are_Equal(arr1, arr2, 5, 5))
