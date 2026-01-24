import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):
    def test_typical_case(self):
        arr1 = [1, 3, 5, 7, 9]
        arr2 = [2, 4, 6, 8, 10]
        n = 5
        self.assertAlmostEqual(get_median(arr1, arr2, n), 5.5)

    def test_edge_case_equal_length(self):
        arr1 = [1, 3, 5, 7, 9]
        arr2 = [2, 4, 6, 8, 9]
        n = 5
        self.assertAlmostEqual(get_median(arr1, arr2, n), 4.5)

    def test_edge_case_diff_length(self):
        arr1 = [1, 3, 5, 7, 9]
        arr2 = [2, 4, 6, 8]
        n = 5
        self.assertAlmostEqual(get_median(arr1, arr2, n), 4.5)

    def test_edge_case_one_array_empty(self):
        arr1 = [1, 3, 5, 7, 9]
        arr2 = []
        n = 5
        with self.assertRaises(IndexError):
            get_median(arr1, arr2, n)

    def test_edge_case_both_arrays_empty(self):
        arr1 = []
        arr2 = []
        n = 5
        with self.assertRaises(IndexError):
            get_median(arr1, arr2, n)
