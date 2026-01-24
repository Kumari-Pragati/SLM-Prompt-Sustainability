import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 3, 20, 4, 1, 0]
        n = len(arr)
        self.assertEqual(find_peak(arr, n), 2)

    def test_edge_condition(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(find_peak(arr, n), 0)

    def test_boundary_condition(self):
        arr = [1, 2]
        n = len(arr)
        self.assertEqual(find_peak(arr, n), 1)

    def test_invalid_input(self):
        arr = []
        n = len(arr)
        with self.assertRaises(ValueError):
            find_peak(arr, n)
