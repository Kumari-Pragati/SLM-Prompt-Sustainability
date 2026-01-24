import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):

    def test_typical_case(self):
        arr1 = [1, 3]
        arr2 = [2]
        n = 2
        self.assertEqual(get_median(arr1, arr2, n), 2.0)

    def test_edge_case_single_element(self):
        arr1 = [1]
        arr2 = [2]
        n = 1
        self.assertEqual(get_median(arr1, arr2, n), 1.5)

    def test_edge_case_empty_arrays(self):
        arr1 = []
        arr2 = [2]
        n = 0
        self.assertEqual(get_median(arr1, arr2, n), 2.0)

    def test_edge_case_same_elements(self):
        arr1 = [1, 2, 3]
        arr2 = [1, 2, 3]
        n = 3
        self.assertEqual(get_median(arr1, arr2, n), 2.0)

    def test_error_case_different_lengths(self):
        arr1 = [1, 2, 3]
        arr2 = [1, 2]
        n = 3
        with self.assertRaises(Exception):
            get_median(arr1, arr2, n)
