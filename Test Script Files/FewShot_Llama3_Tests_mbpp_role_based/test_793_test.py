import unittest
from mbpp_793_code import last

class TestLast(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 5
        n = len(arr)
        self.assertEqual(last(arr, x, n), 4)

    def test_edge_case_low(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 1
        n = len(arr)
        self.assertEqual(last(arr, x, n), 0)

    def test_edge_case_high(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 10
        n = len(arr)
        self.assertEqual(last(arr, x, n), 9)

    def test_invalid_input_array_empty(self):
        arr = []
        x = 5
        n = len(arr)
        with self.assertRaises(IndexError):
            last(arr, x, n)

    def test_invalid_input_array_single_element(self):
        arr = [1]
        x = 1
        n = len(arr)
        self.assertEqual(last(arr, x, n), 0)
