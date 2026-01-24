import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):
    def test_typical_case(self):
        arr = [10, 12, 11, 7, 15]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 3)

    def test_edge_case(self):
        arr = [10, 10, 10, 10, 10]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), n)

    def test_boundary_case(self):
        arr = [10, 9, 8, 7, 6]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 1)

    def test_invalid_input(self):
        arr = [10, 12, 11, 7, 15]
        n = -1
        with self.assertRaises(ValueError):
            max_len_sub(arr, n)
