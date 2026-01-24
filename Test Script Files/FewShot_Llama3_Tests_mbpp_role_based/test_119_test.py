import unittest
from mbpp_119_code import search

class TestSearch(unittest.TestCase):
    def test_search_single_element(self):
        arr = [1]
        n = 1
        self.assertEqual(search(arr, n), 1)

    def test_search_multiple_elements(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        self.assertEqual(search(arr, n), 0)

    def test_search_zero_elements(self):
        arr = []
        n = 0
        self.assertEqual(search(arr, n), 0)

    def test_search_negative_elements(self):
        arr = [-1, -2, -3, -4, -5]
        n = 5
        self.assertEqual(search(arr, n), 0)

    def test_search_non_integer_elements(self):
        arr = [1.0, 2.0, 3.0, 4.0, 5.0]
        n = 5
        self.assertEqual(search(arr, n), 0)
