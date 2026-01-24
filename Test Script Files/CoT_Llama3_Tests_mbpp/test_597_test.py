import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):
    def test_typical_case(self):
        arr1 = [1, 3, 5, 7]
        arr2 = [2, 4, 6, 8]
        m = len(arr1)
        n = len(arr2)
        k = 3
        self.assertEqual(find_kth(arr1, arr2, m, n, k), 5)

    def test_edge_case_k_equal_to_m(self):
        arr1 = [1, 3, 5]
        arr2 = []
        m = len(arr1)
        n = len(arr2)
        k = m
        self.assertEqual(find_kth(arr1, arr2, m, n, k), 5)

    def test_edge_case_k_equal_to_n(self):
        arr1 = []
        arr2 = [1, 3, 5]
        m = len(arr1)
        n = len(arr2)
        k = n
        self.assertEqual(find_kth(arr2, arr1, m, n, k), 3)

    def test_edge_case_k_greater_than_m_n(self):
        arr1 = [1, 3, 5]
        arr2 = [2, 4, 6]
        m = len(arr1)
        n = len(arr2)
        k = m + n + 1
        with self.assertRaises(IndexError):
            find_kth(arr1, arr2, m, n, k)

    def test_edge_case_k_equal_to_zero(self):
        arr1 = [1, 3, 5]
        arr2 = [2, 4, 6]
        m = len(arr1)
        n = len(arr2)
        k = 0
        with self.assertRaises(IndexError):
            find_kth(arr1, arr2, m, n, k)
