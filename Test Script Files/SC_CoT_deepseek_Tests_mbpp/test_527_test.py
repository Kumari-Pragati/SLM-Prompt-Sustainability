import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):
    
    def test_typical_case(self):
        arr = [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 10, 0]
        n = len(arr)
        sum = 10
        self.assertEqual(get_pairs_count(arr, n, sum), 6)

    def test_edge_case_small_array(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 10
        self.assertEqual(get_pairs_count(arr, n, sum), 2)

    def test_edge_case_large_array(self):
        arr = [i for i in range(1, 10001)]
        n = len(arr)
        sum = 10000
        self.assertEqual(get_pairs_count(arr, n, sum), 49995000)

    def test_edge_case_sum_zero(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 0
        self.assertEqual(get_pairs_count(arr, n, sum), 0)

    def test_special_case_negative_numbers(self):
        arr = [-1, -9, -2, -8, -3, -7, -4, -6, -5]
        n = len(arr)
        sum = -10
        self.assertEqual(get_pairs_count(arr, n, sum), 6)

    def test_invalid_input_negative_sum(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = -10
        with self.assertRaises(Exception):
            get_pairs_count(arr, n, sum)
