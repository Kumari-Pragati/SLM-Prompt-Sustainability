import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
        n = 11
        self.assertEqual(find_Diff(arr, n), 2)

    def test_edge_case_empty_array(self):
        arr = []
        n = 0
        self.assertEqual(find_Diff(arr, n), 0)

    def test_edge_case_single_element_array(self):
        arr = [1]
        n = 1
        self.assertEqual(find_Diff(arr, n), 0)

    def test_edge_case_array_with_duplicates(self):
        arr = [1, 1, 2, 2, 3, 3, 3]
        n = 7
        self.assertEqual(find_Diff(arr, n), 2)

    def test_edge_case_array_with_no_duplicates(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        self.assertEqual(find_Diff(arr, n), 0)

    def test_invalid_input_array_length_zero(self):
        arr = []
        n = 5
        with self.assertRaises(IndexError):
            find_Diff(arr, n)

    def test_invalid_input_array_length_negative(self):
        arr = [1, 2, 3]
        n = -5
        with self.assertRaises(ValueError):
            find_Diff(arr, n)
