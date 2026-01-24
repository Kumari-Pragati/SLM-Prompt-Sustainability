import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):
    def test_typical_case(self):
        arr = [5, 2, 8, 3, 1, 6, 4]
        n = len(arr)
        k = 3
        expected = 3
        self.assertEqual(kth_element(arr, n, k), expected)

    def test_edge_case_k1(self):
        arr = [5, 2, 8, 3, 1, 6, 4]
        n = len(arr)
        k = 1
        expected = 5
        self.assertEqual(kth_element(arr, n, k), expected)

    def test_edge_case_kn(self):
        arr = [5, 2, 8, 3, 1, 6, 4]
        n = len(arr)
        k = n
        expected = 4
        self.assertEqual(kth_element(arr, n, k), expected)

    def test_invalid_k(self):
        arr = [5, 2, 8, 3, 1, 6, 4]
        n = len(arr)
        k = n + 1
        with self.assertRaises(IndexError):
            kth_element(arr, n, k)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        k = 1
        with self.assertRaises(IndexError):
            kth_element(arr, n, k)

    def test_single_element_array(self):
        arr = [5]
        n = len(arr)
        k = 1
        expected = 5
        self.assertEqual(kth_element(arr, n, k), expected)
