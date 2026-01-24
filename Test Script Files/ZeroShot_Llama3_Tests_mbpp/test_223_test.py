import unittest
from mbpp_223_code import binary_search

class TestMajority(unittest.TestCase):

    def test_majority_true(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        x = 5
        self.assertTrue(is_majority(arr, n, x))

    def test_majority_false(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        x = 11
        self.assertFalse(is_majority(arr, n, x))

    def test_majority_edge_case(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        x = 5
        self.assertTrue(is_majority(arr, n, x))

    def test_majority_edge_case_false(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        x = 11
        self.assertFalse(is_majority(arr, n, x))

    def test_majority_empty_array(self):
        arr = []
        n = len(arr)
        x = 5
        self.assertFalse(is_majority(arr, n, x))

    def test_majority_single_element_array(self):
        arr = [5]
        n = len(arr)
        x = 5
        self.assertTrue(is_majority(arr, n, x))

    def test_majority_single_element_array_false(self):
        arr = [5]
        n = len(arr)
        x = 6
        self.assertFalse(is_majority(arr, n, x))
