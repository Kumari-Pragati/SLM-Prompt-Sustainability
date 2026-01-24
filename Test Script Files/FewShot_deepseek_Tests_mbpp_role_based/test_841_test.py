import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 9, 6, 4, 5, 8, 7, 3, 2]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 16)

    def test_empty_array(self):
        arr = []
        n = 0
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_reverse_sorted_array(self):
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 36)

    def test_single_element_array(self):
        arr = [5]
        n = 1
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_negative_numbers(self):
        arr = [-1, -9, -6, -4, -5, -8, -7, -3, -2]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 16)

    def test_duplicate_elements(self):
        arr = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 9]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 24)
