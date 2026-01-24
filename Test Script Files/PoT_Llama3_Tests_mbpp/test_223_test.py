import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 5), 4)

    def test_edge_case_low(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 1), 0)

    def test_edge_case_high(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 10), 9)

    def test_edge_case_equal(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 5), 4)

    def test_edge_case_not_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 11), -1)

    def test_edge_case_empty(self):
        arr = []
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 5), -1)

    def test_edge_case_single_element(self):
        arr = [5]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 5), 0)

    def test_edge_case_duplicates(self):
        arr = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(binary_search(arr, 0, len(arr)-1, 2), 1)
