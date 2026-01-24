import unittest
from mbpp_793_code import last

class TestLast(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 3, 5, 7, 9]
        x = 7
        n = len(arr)
        self.assertEqual(last(arr, x, n), 3)

    def test_edge_condition(self):
        arr = [10]
        x = 10
        n = len(arr)
        self.assertEqual(last(arr, x, n), 0)

    def test_boundary_condition(self):
        arr = [1, 3, 5, 7, 9]
        x = 7
        n = 0
        self.assertEqual(last(arr, x, n), -1)

    def test_invalid_input(self):
        arr = [1, 3, 5, 7, 9]
        x = 7
        n = -1
        with self.assertRaises(ValueError):
            last(arr, x, n)
