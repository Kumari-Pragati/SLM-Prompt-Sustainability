import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 9, 6, 4, 5]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 5)

    def test_empty_array(self):
        arr = []
        n = 0
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 10)

    def test_duplicate_elements(self):
        arr = [2, 3, 2, 1]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 2)

    def test_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(get_inv_count(arr, n), 0)
