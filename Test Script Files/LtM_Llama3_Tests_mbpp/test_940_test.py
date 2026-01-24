import unittest
from mbpp_940_code import shift_down

class TestShiftDown(unittest.TestCase):
    def test_shift_down_empty_array(self):
        arr = []
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [])

    def test_shift_down_single_element_array(self):
        arr = [5]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [5])

    def test_shift_down_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_shift_down_unsorted_array(self):
        arr = [5, 2, 8, 3, 1]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 5, 8])

    def test_shift_down_max_value_at_root(self):
        arr = [5, 2, 8, 3, 1]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [8, 5, 3, 2, 1])

    def test_shift_down_min_value_at_root(self):
        arr = [5, 2, 8, 3, 1]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 5, 8])

    def test_shift_down_max_value_at_child(self):
        arr = [5, 2, 8, 3, 1]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [8, 5, 3, 2, 1])

    def test_shift_down_min_value_at_child(self):
        arr = [5, 2, 8, 3, 1]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 5, 8])
