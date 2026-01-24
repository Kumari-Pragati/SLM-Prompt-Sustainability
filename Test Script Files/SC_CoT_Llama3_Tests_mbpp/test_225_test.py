import unittest
from mbpp_225_code import find_Min

class TestFindMin(unittest.TestCase):
    def test_typical_input(self):
        arr = [1, 2, 3, 4, 5]
        low = 0
        high = len(arr) - 1
        self.assertEqual(find_Min(arr, low, high), 1)

    def test_edge_case_equal(self):
        arr = [1, 1, 1, 1, 1]
        low = 0
        high = len(arr) - 1
        self.assertEqual(find_Min(arr, low, high), 1)

    def test_edge_case_min_at_start(self):
        arr = [5, 4, 3, 2, 1]
        low = 0
        high = len(arr) - 1
        self.assertEqual(find_Min(arr, low, high), 1)

    def test_edge_case_min_at_end(self):
        arr = [1, 2, 3, 4, 5]
        low = 0
        high = len(arr) - 1
        self.assertEqual(find_Min(arr, low, high), 5)

    def test_edge_case_min_at_middle(self):
        arr = [5, 4, 3, 2, 1]
        low = 0
        high = len(arr) - 1
        self.assertEqual(find_Min(arr, low, high), 1)

    def test_invalid_input_low_high_out_of_bounds(self):
        arr = [1, 2, 3, 4, 5]
        low = len(arr)
        high = len(arr) - 1
        with self.assertRaises(IndexError):
            find_Min(arr, low, high)

    def test_invalid_input_low_high_negative(self):
        arr = [1, 2, 3, 4, 5]
        low = -1
        high = len(arr) - 1
        with self.assertRaises(IndexError):
            find_Min(arr, low, high)

    def test_invalid_input_low_high_high_lower_than_low(self):
        arr = [1, 2, 3, 4, 5]
        low = 2
        high = 1
        with self.assertRaises(IndexError):
            find_Min(arr, low, high)
