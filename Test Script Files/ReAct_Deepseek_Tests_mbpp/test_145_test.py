import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 9, 11]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 10)

    def test_edge_case_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 0)

    def test_edge_case_negative_elements(self):
        arr = [-1, -3, -9, -11]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 10)

    def test_edge_case_mixed_elements(self):
        arr = [-1, 3, -9, 11]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 14)

    def test_error_case_empty_array(self):
        arr = []
        n = len(arr)
        with self.assertRaises(IndexError):
            max_Abs_Diff(arr, n)
