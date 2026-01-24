import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 5)

    def test_edge_case(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 1)

    def test_boundary_case(self):
        arr = [1, 2, 3, 4, 5, 6]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 6)

    def test_invalid_input(self):
        arr = [1, 2, 3]
        n ='string'
        with self.assertRaises(TypeError):
            max_len_sub(arr, n)
