import unittest

from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 4
        result = binary_search(arr, 0, n-1, x)
        self.assertEqual(result, 3)

    def test_edge_case_low(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 1
        result = binary_search(arr, 0, n-1, x)
        self.assertEqual(result, 0)

    def test_edge_case_high(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 5
        result = binary_search(arr, 0, n-1, x)
        self.assertEqual(result, 4)

    def test_corner_case_not_present(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 6
        result = binary_search(arr, 0, n-1, x)
        self.assertEqual(result, -1)

    def test_corner_case_empty_array(self):
        arr = []
        n = len(arr)
        x = 1
        result = binary_search(arr, 0, n-1, x)
        self.assertEqual(result, -1)
