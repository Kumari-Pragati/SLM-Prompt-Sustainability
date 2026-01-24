import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 4, 9, 10, 11, 12, 17]
        n = len(arr)
        k = 4
        self.assertEqual(removals(arr, n, k), 2)

    def test_single_element(self):
        arr = [5]
        n = len(arr)
        k = 10
        self.assertEqual(removals(arr, n, k), 0)

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 1
        self.assertEqual(removals(arr, n, k), 1)

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        k = 1
        self.assertEqual(removals(arr, n, k), 1)

    def test_large_k(self):
        arr = [1, 3, 4, 9, 10, 11, 12, 17]
        n = len(arr)
        k = 15
        self.assertEqual(removals(arr, n, k), 0)

    def test_negative_numbers(self):
        arr = [-5, -3, -2, -1, 0, 1, 2, 3]
        n = len(arr)
        k = 2
        self.assertEqual(removals(arr, n, k), 2)

    def test_duplicate_numbers(self):
        arr = [1, 2, 2, 3, 4, 4, 5, 6]
        n = len(arr)
        k = 1
        self.assertEqual(removals(arr, n, k), 2)
