import unittest
from mbpp_195_code import first

class TestFirstFunction(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), 4)

    def test_edge_case(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 10
        n = len(arr)
        self.assertEqual(first(arr, x, n), 9)

    def test_edge_case2(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 1
        n = len(arr)
        self.assertEqual(first(arr, x, n), 0)

    def test_edge_case3(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 11
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = "a"
        n = len(arr)
        with self.assertRaises(TypeError):
            first(arr, x, n)
