import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_typical_case(self):
        arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 5)

    def test_edge_case(self):
        arr = [10]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 1)

    def test_boundary_case(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 0)

    def test_special_case(self):
        arr = [10, 22, 9, 33, 21, 50, 41, 60, 80, 70, 65, 64]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 5)

    def test_invalid_input(self):
        arr = [10, 22, 'a', 33, 21, 50, 41, 60, 80]
        n = len(arr)
        with self.assertRaises(TypeError):
            max_len_sub(arr, n)
