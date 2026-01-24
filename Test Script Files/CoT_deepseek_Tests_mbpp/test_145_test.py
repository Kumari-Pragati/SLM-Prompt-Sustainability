import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 9, 11]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 10)

    def test_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 0)

    def test_negative_numbers(self):
        arr = [-1, -3, -9, -11]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 10)

    def test_mixed_numbers(self):
        arr = [-1, 3, -9, 11]
        n = len(arr)
        self.assertEqual(max_Abs_Diff(arr, n), 14)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        with self.assertRaises(IndexError):
            max_Abs_Diff(arr, n)

    def test_invalid_input(self):
        arr = [1, 2, 3]
        n = -1
        with self.assertRaises(ValueError):
            max_Abs_Diff(arr, n)
