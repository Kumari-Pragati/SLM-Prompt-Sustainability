import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 4)

    def test_edge_case_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 0)

    def test_edge_case_all_equal(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 0)

    def test_edge_case_all_negative(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 4)

    def test_edge_case_all_positive(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 4)

    def test_invalid_input_empty_array(self):
        arr = []
        n = len(arr)
        with self.assertRaises(IndexError):
            max_Abs_Diff(arr, n)
