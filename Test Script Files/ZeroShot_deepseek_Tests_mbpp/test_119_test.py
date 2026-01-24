import unittest
from mbpp_119_code import search

class TestSearchFunction(unittest.TestCase):

    def test_search_with_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(search(arr, n), 1^2^3^4^5)

    def test_search_with_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(search(arr, n), -1^(-2)^(-3)^(-4)^(-5))

    def test_search_with_mixed_numbers(self):
        arr = [1, -2, 3, -4, 5]
        n = len(arr)
        self.assertEqual(search(arr, n), 1^(-2)^3^(-4)^5)

    def test_search_with_zero(self):
        arr = [0, 1, 2, 3, 4]
        n = len(arr)
        self.assertEqual(search(arr, n), 0^1^2^3^4)

    def test_search_with_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(search(arr, n), 0)
