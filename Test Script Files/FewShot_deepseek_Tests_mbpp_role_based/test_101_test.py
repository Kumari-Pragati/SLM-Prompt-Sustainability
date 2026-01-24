import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [7, 10, 4, 3, 20, 15]
        n = len(arr)
        k = 3
        self.assertEqual(kth_element(arr, n, k), 10)

    def test_edge_case(self):
        arr = [7]
        n = len(arr)
        k = 1
        self.assertEqual(kth_element(arr, n, k), 7)

    def test_boundary_case(self):
        arr = [7, 10, 4, 3, 20, 15]
        n = len(arr)
        k = n
        self.assertEqual(kth_element(arr, n, k), 20)

    def test_invalid_input(self):
        arr = [7, 10, 4, 3, 20, 15]
        n = len(arr)
        k = n + 1
        with self.assertRaises(IndexError):
            kth_element(arr, n, k)
