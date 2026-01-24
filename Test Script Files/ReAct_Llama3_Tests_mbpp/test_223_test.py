import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_majority_true(self):
        arr = [1, 2, 3, 4, 5, 5, 5, 5, 5]
        n = len(arr)
        x = 5
        self.assertTrue(is_majority(arr, n, x))

    def test_majority_false(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        n = len(arr)
        x = 10
        self.assertFalse(is_majority(arr, n, x))

    def test_majority_edge_case(self):
        arr = [1, 2, 3, 4, 5, 5, 5, 5, 5]
        n = len(arr)
        x = 5
        self.assertTrue(is_majority(arr, n, x))

    def test_binary_search_edge_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 5
        self.assertEqual(binary_search(arr, 0, n-1, x), 4)

    def test_binary_search_edge_case2(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 1
        self.assertEqual(binary_search(arr, 0, n-1, x), 0)

    def test_binary_search_edge_case3(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 6
        self.assertEqual(binary_search(arr, 0, n-1, x), -1)

    def test_binary_search_edge_case4(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 5
        self.assertEqual(binary_search(arr, 0, n-1, x), 4)

    def test_binary_search_edge_case5(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 1
        self.assertEqual(binary_search(arr, 0, n-1, x), 0)

    def test_binary_search_edge_case6(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 6
        self.assertEqual(binary_search(arr, 0, n-1, x), -1)

    def test_binary_search_edge_case7(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 5
        self.assertEqual(binary_search(arr, 0, n-1, x), 4)

    def test_binary_search_edge_case8(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 1
        self.assertEqual(binary_search(arr, 0, n-1, x), 0)

    def test_binary_search_edge_case9(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 6
        self.assertEqual(binary_search(arr, 0, n-1, x), -1)

    def test_binary_search_edge_case10(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 5
        self.assertEqual(binary_search(arr, 0, n-1, x), 4)

    def test_binary_search_edge_case11(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 1
        self.assertEqual(binary_search(arr, 0, n-1, x), 0)

    def test_binary_search_edge_case12(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 6
        self.assertEqual(binary_search(arr, 0, n-1, x), -1)

    def test_binary_search_edge_case13(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 5
        self.assertEqual(binary_search(arr, 0, n-1, x), 4)

    def test_binary_search_edge_case14(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 1
        self.assertEqual(binary_search(arr, 0, n