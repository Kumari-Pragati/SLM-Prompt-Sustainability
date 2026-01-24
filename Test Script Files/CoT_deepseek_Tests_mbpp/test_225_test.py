import unittest
from mbpp_225_code import find_Min

class TestFindMin(unittest.TestCase):

    def test_typical_case(self):
        arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 1)

    def test_single_element(self):
        arr = [4]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 4)

    def test_duplicate_elements(self):
        arr = [4, 4, 4, 4, 4]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 4)

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 1)

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(find_Min(arr, 0, len(arr) - 1), 1)

    def test_empty_array(self):
        arr = []
        with self.assertRaises(IndexError):
            find_Min(arr, 0, len(arr) - 1)

    def test_invalid_low_high(self):
        arr = [1, 2, 3, 4, 5]
        with self.assertRaises(IndexError):
            find_Min(arr, 5, 0)
