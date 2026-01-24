import unittest
from mbpp_223_code import is_majority, binary_search

class TestIsMajority(unittest.TestCase):

    def test_is_majority_true(self):
        arr = [1, 2, 2, 2, 3, 4]
        n = len(arr)
        x = 2
        self.assertTrue(is_majority(arr, n, x))

    def test_is_majority_false(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 2
        self.assertFalse(is_majority(arr, n, x))

    def test_binary_search_true(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 4
        self.assertEqual(binary_search(arr, 0, n-1, x), 3)

    def test_binary_search_false(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 6
        self.assertEqual(binary_search(arr, 0, n-1, x), -1)
