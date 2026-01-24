import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_sum(arr, n), 15)

    def test_edge_case(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(max_sum(arr, n), 1)

    def test_boundary_case(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        self.assertEqual(max_sum(arr, n), 55)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4, 5]
        n = -1
        with self.assertRaises(ValueError):
            max_sum(arr, n)

    def test_invalid_input_2(self):
        arr = []
        n = 0
        with self.assertRaises(ValueError):
            max_sum(arr, n)
