import unittest
from mbpp_793_code import last

class TestLastFunction(unittest.TestCase):

    def test_typical_input(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 5
        n = len(arr)
        self.assertEqual(last(arr, x, n), 4)

    def test_edge_case(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 1
        n = len(arr)
        self.assertEqual(last(arr, x, n), 0)

    def test_edge_case2(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 10
        n = len(arr)
        self.assertEqual(last(arr, x, n), 9)

    def test_edge_case3(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 10
        n = 1
        self.assertEqual(last(arr, x, n), -1)

    def test_edge_case4(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 0
        n = len(arr)
        self.assertEqual(last(arr, x, n), -1)

    def test_edge_case5(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 11
        n = len(arr)
        self.assertEqual(last(arr, x, n), -1)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = "string"
        n = len(arr)
        with self.assertRaises(TypeError):
            last(arr, x, n)
