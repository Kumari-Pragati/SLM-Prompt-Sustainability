import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(find_Max(arr, 0, len(arr) - 1), 9)

    def test_edge_case_single_element(self):
        arr = [5]
        self.assertEqual(find_Max(arr, 0, len(arr) - 1), 5)

    def test_edge_case_two_elements(self):
        arr = [5, 10]
        self.assertEqual(find_Max(arr, 0, len(arr) - 1), 10)

    def test_edge_case_decreasing_order(self):
        arr = [9, 7, 5, 3, 1]
        self.assertEqual(find_Max(arr, 0, len(arr) - 1), 9)

    def test_error_case_empty_array(self):
        arr = []
        with self.assertRaises(IndexError):
            find_Max(arr, 0, len(arr) - 1)

    def test_error_case_invalid_low_high(self):
        arr = [1, 3, 5, 7, 9]
        with self.assertRaises(AssertionError):
            find_Max(arr, 5, 1)
