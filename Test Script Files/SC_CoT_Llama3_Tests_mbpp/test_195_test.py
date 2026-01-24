import unittest
from mbpp_195_code import first

class TestFirstFunction(unittest.TestCase):
    def test_typical_input(self):
        arr = [1, 2, 3, 4, 5]
        x = 3
        n = len(arr)
        self.assertEqual(first(arr, x, n), 2)

    def test_edge_case(self):
        arr = [1, 2, 3, 4, 5]
        x = 1
        n = len(arr)
        self.assertEqual(first(arr, x, n), 0)

    def test_edge_case2(self):
        arr = [1, 2, 3, 4, 5]
        x = 5
        n = len(arr)
        self.assertEqual(first(arr, x, n), 4)

    def test_edge_case3(self):
        arr = [1, 2, 3, 4, 5]
        x = 6
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

    def test_edge_case4(self):
        arr = [1, 2, 3, 4, 5]
        x = 0
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

    def test_edge_case5(self):
        arr = [1, 2, 3, 4, 5]
        x = 5.5
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

    def test_edge_case6(self):
        arr = [1, 2, 3, 4, 5]
        x = 'a'
        n = len(arr)
        with self.assertRaises(TypeError):
            first(arr, x, n)

    def test_edge_case7(self):
        arr = [1, 2, 3, 4, 5]
        x = None
        n = len(arr)
        with self.assertRaises(TypeError):
            first(arr, x, n)
