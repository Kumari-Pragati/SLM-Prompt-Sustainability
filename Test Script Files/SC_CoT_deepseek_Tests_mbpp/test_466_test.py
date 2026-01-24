import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 20, 4, 1, 0]
        self.assertEqual(find_peak(arr, len(arr)), 2)

    def test_edge_case_single_element(self):
        arr = [1]
        self.assertEqual(find_peak(arr, len(arr)), 0)

    def test_edge_case_two_elements(self):
        arr = [2, 1]
        self.assertEqual(find_peak(arr, len(arr)), 0)

    def test_corner_case_decreasing_sequence(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(find_peak(arr, len(arr)), 0)

    def test_corner_case_increasing_sequence(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_peak(arr, len(arr)), 4)

    def test_invalid_input_empty_array(self):
        arr = []
        with self.assertRaises(IndexError):
            find_peak(arr, len(arr))

    def test_invalid_input_non_list(self):
        arr = "not a list"
        with self.assertRaises(TypeError):
            find_peak(arr, len(arr))
