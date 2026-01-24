import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 7, 5, 9, 2, 12, 3, 2]
        n = len(arr)
        k = 2
        self.assertEqual(count_pairs(arr, n, k), 3)

    def test_edge_case(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        k = 0
        self.assertEqual(count_pairs(arr, n, k), 10)

    def test_boundary_case(self):
        arr = [1]
        n = len(arr)
        k = 1
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_special_case(self):
        arr = [10, 20, 30, 40, 50]
        n = len(arr)
        k = 10
        self.assertEqual(count_pairs(arr, n, k), 4)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4, 5]
        n = -1
        k = 1
        with self.assertRaises(Exception):
            count_pairs(arr, n, k)
