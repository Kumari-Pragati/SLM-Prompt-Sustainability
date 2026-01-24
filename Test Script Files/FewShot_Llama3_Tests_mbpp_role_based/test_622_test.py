import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):
    def test_typical_use_case(self):
        arr1 = [1, 3, 5, 7, 9]
        arr2 = [2, 4, 6, 8, 10]
        n = 5
        self.assertAlmostEqual(get_median(arr1, arr2, n), 5.5)

    def test_edge_case_equal_lengths(self):
        arr1 = [1, 3, 5, 7, 9]
        arr2 = [2, 4, 6, 8, 9]
        n = 5
        self.assertAlmostEqual(get_median(arr1, arr2, n), 5.5)

    def test_edge_case_diff_lengths(self):
        arr1 = [1, 3, 5, 7, 9]
        arr2 = [2, 4, 6, 8]
        n = 5
        self.assertAlmostEqual(get_median(arr1, arr2, n), 5.5)

    def test_edge_case_one_array_empty(self):
        arr1 = [1, 3, 5, 7, 9]
        arr2 = []
        n = 5
        self.assertAlmostEqual(get_median(arr1, arr2, n), 5.5)

    def test_edge_case_two_arrays_empty(self):
        arr1 = []
        arr2 = []
        n = 5
        self.assertEqual(get_median(arr1, arr2, n), -1)

    def test_invalid_input_type(self):
        arr1 = [1, 3, 5, 7, 9]
        arr2 = "Invalid input"
        n = 5
        with self.assertRaises(TypeError):
            get_median(arr1, arr2, n)
