import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):
    def test_kth_element_positive_array(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(kth_element(arr, n, 3), 3)

    def test_kth_element_negative_array(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(kth_element(arr, n, 3), -3)

    def test_kth_element_zero_array(self):
        arr = [0, 0, 0, 0, 0]
        n = len(arr)
        self.assertEqual(kth_element(arr, n, 3), 0)

    def test_kth_element_invalid_k(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        with self.assertRaises(IndexError):
            kth_element(arr, n, 6)

    def test_kth_element_empty_array(self):
        arr = []
        n = len(arr)
        with self.assertRaises(IndexError):
            kth_element(arr, n, 1)
