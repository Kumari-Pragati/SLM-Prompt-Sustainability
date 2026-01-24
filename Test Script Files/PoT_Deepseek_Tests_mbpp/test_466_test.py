import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 20, 4, 1, 0]
        self.assertEqual(find_peak(arr, len(arr)), 2)

    def test_edge_case_single_element(self):
        arr = [5]
        self.assertEqual(find_peak(arr, len(arr)), 0)

    def test_boundary_case_ascending_order(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_peak(arr, len(arr)), 4)

    def test_boundary_case_descending_order(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(find_peak(arr, len(arr)), 0)

    def test_corner_case_repeated_elements(self):
        arr = [1, 1, 1, 1, 1]
        self.assertEqual(find_peak(arr, len(arr)), 0)

    def test_corner_case_all_elements_same(self):
        arr = [5, 5, 5, 5, 5]
        self.assertEqual(find_peak(arr, len(arr)), 0)

    def test_corner_case_empty_array(self):
        arr = []
        with self.assertRaises(IndexError):
            find_peak(arr, 0)
