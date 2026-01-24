import unittest
from mbpp_195_code import first

class TestFirstFunction(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), 4)

    def test_edge_case_lower(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 0
        n = len(arr)
        self.assertEqual(first(arr, x, n), 0)

    def test_edge_case_higher(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 11
        n = len(arr)
        self.assertEqual(first(arr, x, n), 9)

    def test_edge_case_equal(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), 4)

    def test_empty_array(self):
        arr = []
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

    def test_single_element_array(self):
        arr = [5]
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), 0)

    def test_array_with_duplicates(self):
        arr = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), 4)
