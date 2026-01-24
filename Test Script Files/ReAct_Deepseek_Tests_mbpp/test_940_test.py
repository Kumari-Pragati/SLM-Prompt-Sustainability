import unittest
from mbpp_940_code import shift_down

class TestShiftDown(unittest.TestCase):

    def test_typical_case(self):
        arr = [3, 2, 1, 5, 4]
        shift_down(arr, 0, 4)
        self.assertEqual(arr, [5, 2, 1, 4, 3])

    def test_edge_case_single_element(self):
        arr = [1]
        shift_down(arr, 0, 0)
        self.assertEqual(arr, [1])

    def test_edge_case_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        shift_down(arr, 0, 4)
        self.assertEqual(arr, [5, 2, 3, 4, 1])

    def test_error_case_empty_array(self):
        arr = []
        with self.assertRaises(IndexError):
            shift_down(arr, 0, -1)

    def test_error_case_negative_indices(self):
        arr = [1, 2, 3, 4, 5]
        with self.assertRaises(IndexError):
            shift_down(arr, -1, 4)

    def test_error_case_out_of_range_indices(self):
        arr = [1, 2, 3, 4, 5]
        with self.assertRaises(IndexError):
            shift_down(arr, 0, 10)
