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

    def test_shift_down_two_elements_array(self):
        arr = [5, 3]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [5, 3])

    def test_shift_down_three_elements_array(self):
        arr = [5, 3, 2]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [5, 3, 2])

    def test_shift_down_large_array(self):
        arr = [5, 3, 2, 7, 1, 9, 8, 6, 4]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_shift_down_array_with_duplicates(self):
        arr = [5, 3, 2, 7, 1, 9, 8, 6, 4, 5, 3, 2]
        shift_down(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [9, 8, 7, 6, 5, 5, 4, 3, 3, 2, 2, 1])
