import unittest
from mbpp_119_code import search

class TestSearchFunction(unittest.TestCase):

    def test_typical_input(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(search(arr, n), 0)

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(search(arr, n), 0)

    def test_edge_case_single_element_array(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(search(arr, n), 1)

    def test_edge_case_zero_length_array(self):
        arr = []
        n = 0
        self.assertEqual(search(arr, n), 0)

    def test_edge_case_negative_length(self):
        arr = [1, 2, 3, 4, 5]
        n = -1
        with self.assertRaises(TypeError):
            search(arr, n)

    def test_edge_case_non_integer_length(self):
        arr = [1, 2, 3, 4, 5]
        n = 'a'
        with self.assertRaises(TypeError):
            search(arr, n)

    def test_edge_case_non_integer_array_element(self):
        arr = [1, 2, 'a', 4, 5]
        n = len(arr)
        with self.assertRaises(TypeError):
            search(arr, n)

    def test_edge_case_non_array_input(self):
        arr = 'abc'
        n = len(arr)
        with self.assertRaises(TypeError):
            search(arr, n)
