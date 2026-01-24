import unittest
from mbpp_195_code import first

class TestFirst(unittest.TestCase):
    def test_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), 4)

    def test_not_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 11
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

    def test_edge_case(self):
        arr = [1, 2, 3, 4, 5]
        x = 1
        n = len(arr)
        self.assertEqual(first(arr, x, n), 0)

    def test_empty_array(self):
        arr = []
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4, 5]
        x = "five"
        n = len(arr)
        with self.assertRaises(TypeError):
            first(arr, x, n)
