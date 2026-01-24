import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):

    def test_find_kth_simple(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [6, 7, 8, 9]
        m = len(arr1)
        n = len(arr2)
        k = 5
        self.assertEqual(find_kth(arr1, arr2, m, n, k), 5)

    def test_find_kth_reverse(self):
        arr1 = [10, 9, 8, 7]
        arr2 = [1, 2, 3, 4]
        m = len(arr1)
        n = len(arr2)
        k = 1
        self.assertEqual(find_kth(arr1, arr2, m, n, k), 1)

    def test_find_kth_edge_case(self):
        arr1 = [1]
        arr2 = [2, 3, 4]
        m = len(arr1)
        n = len(arr2)
        k = 1
        self.assertEqual(find_kth(arr1, arr2, m, n, k), 2)

    def test_find_kth_empty(self):
        arr1 = []
        arr2 = [1]
        m = len(arr1)
        n = len(arr2)
        k = 1
        self.assertEqual(find_kth(arr1, arr2, m, n, k), 1)

    def test_find_kth_single_array(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = []
        m = len(arr1)
        n = 0
        k = 1
        self.assertEqual(find_kth(arr1, arr2, m, n, k), 1)
