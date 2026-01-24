import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 3, 5, 7, 9]
        n = len(arr)
        self.assertEqual(find_Min_Diff(arr, n), 2)

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        with self.assertRaises(IndexError):
            find_Min_Diff(arr, n)

    def test_edge_case_single_element_array(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(find_Min_Diff(arr, n), 10**20)

    def test_edge_case_two_element_array(self):
        arr = [1, 2]
        n = len(arr)
        self.assertEqual(find_Min_Diff(arr, n), 1)

    def test_edge_case_large_diff(self):
        arr = [1, 10, 20, 30, 40]
        n = len(arr)
        self.assertEqual(find_Min_Diff(arr, n), 9)

    def test_edge_case_negative_numbers(self):
        arr = [-5, -3, -1, 0, 1]
        n = len(arr)
        self.assertEqual(find_Min_Diff(arr, n), 2)
