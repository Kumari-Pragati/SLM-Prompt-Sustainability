import unittest
from mbpp_650_code import are_Equal

class TestAreEqual(unittest.TestCase):
    def test_typical_case(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 3, 4, 5]
        self.assertTrue(are_Equal(arr1, arr2, len(arr1), len(arr2)))

    def test_different_lengths(self):
        arr1 = [1, 2, 3]
        arr2 = [1, 2, 3, 4]
        self.assertFalse(are_Equal(arr1, arr2, len(arr1), len(arr2)))

    def test_different_contents(self):
        arr1 = [1, 2, 3]
        arr2 = [1, 2, 4]
        self.assertFalse(are_Equal(arr1, arr2, len(arr1), len(arr2)))

    def test_empty_arrays(self):
        arr1 = []
        arr2 = []
        self.assertTrue(are_Equal(arr1, arr2, len(arr1), len(arr2)))

    def test_single_element_arrays(self):
        arr1 = [1]
        arr2 = [1]
        self.assertTrue(are_Equal(arr1, arr2, len(arr1), len(arr2)))

    def test_negative_numbers(self):
        arr1 = [-1, -2, -3]
        arr2 = [-1, -2, -3]
        self.assertTrue(are_Equal(arr1, arr2, len(arr1), len(arr2)))

    def test_duplicate_elements(self):
        arr1 = [1, 2, 2]
        arr2 = [1, 2, 2]
        self.assertTrue(are_Equal(arr1, arr2, len(arr1), len(arr2)))
