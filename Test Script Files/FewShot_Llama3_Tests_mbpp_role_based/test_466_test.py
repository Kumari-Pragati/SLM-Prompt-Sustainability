import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_peak(arr, len(arr)), 4)

    def test_edge_case_low(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_peak(arr, len(arr)), 4)

    def test_edge_case_high(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_peak(arr, len(arr)), 4)

    def test_edge_case_single_element(self):
        arr = [1]
        self.assertEqual(find_peak(arr, len(arr)), 0)

    def test_edge_case_empty_array(self):
        arr = []
        with self.assertRaises(IndexError):
            find_peak(arr, len(arr))

    def test_invalid_input_non_integer(self):
        arr = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            find_peak(arr, 'a')
