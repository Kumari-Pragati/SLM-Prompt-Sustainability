import unittest
from mbpp_564_code import count_Pairs

class TestCountPairs(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 6)

    def test_edge_condition(self):
        arr = []
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_boundary_condition(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_all_same_elements(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 0)

    def test_all_different_elements(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(count_Pairs(arr, n), 10)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4, 5]
        n = -1
        with self.assertRaises(Exception):
            count_Pairs(arr, n)
