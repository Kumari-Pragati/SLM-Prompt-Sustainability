import unittest
from mbpp_119_code import search

class TestSearchFunction(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        result = search(arr, n)
        self.assertEqual(result, 1^2^3^4^5)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        result = search(arr, n)
        self.assertEqual(result, 0)

    def test_single_element_array(self):
        arr = [10]
        n = len(arr)
        result = search(arr, n)
        self.assertEqual(result, 10)

    def test_duplicate_elements(self):
        arr = [1, 2, 2, 1]
        n = len(arr)
        result = search(arr, n)
        self.assertEqual(result, 0)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        result = search(arr, n)
        self.assertEqual(result, -1^-2^-3^-4^-5)

    def test_large_numbers(self):
        arr = [1000000000, 2000000000, 3000000000]
        n = len(arr)
        result = search(arr, n)
        self.assertEqual(result, 1000000000^2000000000^3000000000)
