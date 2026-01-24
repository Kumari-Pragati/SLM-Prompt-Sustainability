import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):

    def test_typical_case(self):
        arr1 = [1, 3, 5]
        arr2 = [2, 4, 6]
        m = len(arr1)
        n = len(arr2)
        k = 5
        self.assertEqual(find_kth(arr1, arr2, m, n, k), 4)

    def test_edge_case(self):
        arr1 = [1, 3, 5]
        arr2 = [2, 4, 6]
        m = len(arr1)
        n = len(arr2)
        k = 1
        self.assertEqual(find_kth(arr1, arr2, m, n, k), 1)

    def test_boundary_case(self):
        arr1 = [1, 3, 5]
        arr2 = [2, 4, 6]
        m = len(arr1)
        n = len(arr2)
        k = m + n
        self.assertEqual(find_kth(arr1, arr2, m, n, k), 6)

    def test_invalid_k(self):
        arr1 = [1, 3, 5]
        arr2 = [2, 4, 6]
        m = len(arr1)
        n = len(arr2)
        k = 0
        with self.assertRaises(IndexError):
            find_kth(arr1, arr2, m, n, k)

    def test_empty_arrays(self):
        arr1 = []
        arr2 = [2, 4, 6]
        m = len(arr1)
        n = len(arr2)
        k = 1
        self.assertEqual(find_kth(arr1, arr2, m, n, k), arr2[0])
