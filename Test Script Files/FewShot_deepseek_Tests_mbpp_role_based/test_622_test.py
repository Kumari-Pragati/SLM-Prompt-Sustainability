import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):
    def test_typical_case(self):
        arr1 = [1, 3]
        arr2 = [2]
        n = 2
        self.assertEqual(get_median(arr1, arr2, n), 2.0)

    def test_edge_case(self):
        arr1 = [1]
        arr2 = [2, 3, 4, 5, 6]
        n = 1
        self.assertEqual(get_median(arr1, arr2, n), 2.0)

    def test_boundary_case(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [6, 7, 8, 9, 10]
        n = 5
        self.assertEqual(get_median(arr1, arr2, n), 5.5)

    def test_invalid_input(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 5]
        n = 6
        with self.assertRaises(IndexError):
            get_median(arr1, arr2, n)
