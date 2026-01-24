import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 7, 5, 9, 2, 12, 3, 2]
        n = len(arr)
        k = 2
        self.assertEqual(count_pairs(arr, n, k), 3)

    def test_edge_case(self):
        arr = [1]
        n = len(arr)
        k = 0
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_boundary_case(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        k = 1
        self.assertEqual(count_pairs(arr, n, k), 45)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        k = 'a'
        with self.assertRaises(TypeError):
            count_pairs(arr, n, k)
