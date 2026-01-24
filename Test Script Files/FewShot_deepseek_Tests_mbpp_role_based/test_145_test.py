import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 4)

    def test_edge_case_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 0)

    def test_boundary_case_min_max(self):
        arr = [1, 100]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 99)

    def test_boundary_case_negative_numbers(self):
        arr = [-10, -5]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 5)

    def test_invalid_input_empty_array(self):
        arr = []
        n = len(arr)
        with self.assertRaises(ValueError):
            max_Abs_Diff(arr, n)
