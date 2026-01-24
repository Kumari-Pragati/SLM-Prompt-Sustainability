import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(sum_Pairs(arr, n), 0)

    def test_edge_condition(self):
        arr = []
        n = 0
        self.assertEqual(sum_Pairs(arr, n), 0)

    def test_boundary_condition(self):
        arr = [1]
        n = 1
        self.assertEqual(sum_Pairs(arr, n), 0)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4, 5]
        n = -1
        with self.assertRaises(Exception):
            sum_Pairs(arr, n)
