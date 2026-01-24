import unittest
from mbpp_195_code import first

class TestFirst(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        x = 3
        n = len(arr)
        self.assertEqual(first(arr, x, n), 2)

    def test_edge_condition(self):
        arr = [1]
        x = 1
        n = len(arr)
        self.assertEqual(first(arr, x, n), 0)

    def test_boundary_condition(self):
        arr = [1, 2, 3, 4, 5]
        x = 6
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4, 5]
        x = 3
        n = -1
        with self.assertRaises(IndexError):
            first(arr, x, n)
