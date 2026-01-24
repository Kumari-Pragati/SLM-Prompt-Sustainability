import unittest
from mbpp_940_code import shift_down

class TestShiftDown(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [5, 3, 8, 6, 1, 9, 2, 7, 4]
        shift_down(arr, 0, len(arr) - 1)
        expected = [3, 5, 1, 6, 8, 2, 7, 9, 4]
        self.assertEqual(arr, expected)

    def test_empty_list(self):
        self.assertRaises(IndexError, lambda: shift_down([], 0, len([]) - 1))

    def test_single_element_list(self):
        self.assertRaises(IndexError, lambda: shift_down([1], 0, len([1]) - 1))

    def test_one_level_down(self):
        arr = [5, 3, 8]
        shift_down(arr, 0, 1)
        expected = [3, 5]
        self.assertEqual(arr, expected)

    def test_max_depth_heap(self):
        arr = [1, 2, 3, 4, 5]
        shift_down(arr, 0, len(arr) - 1)
        expected = [2, 1, 5, 3, 4]
        self.assertEqual(arr, expected)
