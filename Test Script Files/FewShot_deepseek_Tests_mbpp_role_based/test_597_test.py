import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):
    def test_typical_use_case(self):
        arr1 = [1, 3, 5]
        arr2 = [2, 4, 6]
        m = len(arr1)
        n = len(arr2)
        k = 3
        self.assertEqual(find_kth(arr1, arr2, m, n, k), 4)

    def test_boundary_conditions(self):
        arr1 = [1]
        arr2 = [2, 3, 4]
        m = len(arr1)
        n = len(arr2)
        k = 1
        self.assertEqual(find_kth(arr1, arr2, m, n, k), 1)

        arr1 = [1, 2, 3, 4]
        arr2 = [5]
        m = len(arr1)
        n = len(arr2)
        k = 5
        self.assertEqual(find_kth(arr1, arr2, m, n, k), 5)

    def test_edge_conditions(self):
        arr1 = []
        arr2 = [1, 2, 3]
        m = len(arr1)
        n = len(arr2)
        k = 1
        self.assertEqual(find_kth(arr1, arr2, m, n, k), 1)

        arr1 = [1, 2, 3]
        arr2 = []
        m = len(arr1)
        n = len(arr2)
        k = 1
        self.assertEqual(find_kth(arr1, arr2, m, n, k), 1)

    def test_invalid_inputs(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        m = len(arr1)
        n = len(arr2)
        k = 0
        with self.assertRaises(IndexError):
            find_kth(arr1, arr2, m, n, k)

        k = 8
        with self.assertRaises(IndexError):
            find_kth(arr1, arr2, m, n, k)
