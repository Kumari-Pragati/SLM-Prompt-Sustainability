import unittest
from mbpp_195_code import first

class TestFirstFunction(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 5, 7, 9]
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), 2)

    def test_edge_case_not_found(self):
        arr = [1, 3, 5, 7, 9]
        x = 10
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

    def test_edge_case_empty_array(self):
        arr = []
        x = 5
        n = 0
        self.assertEqual(first(arr, x, n), -1)

    def test_edge_case_single_element(self):
        arr = [5]
        x = 5
        n = 1
        self.assertEqual(first(arr, x, n), 0)

    def test_edge_case_duplicates(self):
        arr = [1, 3, 5, 5, 7, 9]
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), 2)

    def test_invalid_input_negative_index(self):
        arr = [1, 3, 5, 7, 9]
        x = 5
        n = -1
        with self.assertRaises(IndexError):
            first(arr, x, n)

    def test_invalid_input_non_integer_index(self):
        arr = [1, 3, 5, 7, 9]
        x = 5
        n = "five"
        with self.assertRaises(TypeError):
            first(arr, x, n)
