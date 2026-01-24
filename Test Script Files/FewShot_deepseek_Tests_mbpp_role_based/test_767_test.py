import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 5, 7, -1]
        n = len(arr)
        sum = 6
        self.assertEqual(get_Pairs_Count(arr, n, sum), 1)

    def test_edge_case(self):
        arr = [1, 1, 1, 1]
        n = len(arr)
        sum = 2
        self.assertEqual(get_Pairs_Count(arr, n, sum), 6)

    def test_boundary_case(self):
        arr = [0, 0, 0, 0]
        n = len(arr)
        sum = 0
        self.assertEqual(get_Pairs_Count(arr, n, sum), 6)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4]
        n = -1
        sum = 5
        with self.assertRaises(Exception):
            get_Pairs_Count(arr, n, sum)
