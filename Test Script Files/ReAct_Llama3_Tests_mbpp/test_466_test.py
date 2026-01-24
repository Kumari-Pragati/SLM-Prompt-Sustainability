import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_peak(arr, len(arr)), 2)

    def test_edge_case_low(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_peak(arr, 1), 1)

    def test_edge_case_high(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_peak(arr, len(arr) - 1), len(arr) - 1)

    def test_edge_case_equal(self):
        arr = [1, 1, 1, 1, 1]
        self.assertEqual(find_peak(arr, len(arr)), 0)

    def test_edge_case_single(self):
        arr = [1]
        self.assertEqual(find_peak(arr, len(arr)), 0)

    def test_edge_case_empty(self):
        arr = []
        with self.assertRaises(IndexError):
            find_peak(arr, len(arr))
