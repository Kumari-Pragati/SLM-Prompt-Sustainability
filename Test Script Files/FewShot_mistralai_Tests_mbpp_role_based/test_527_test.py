import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):
    def test_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 3
        self.assertEqual(get_pairs_count(arr, n, sum), 1)

    def test_zero_sum(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 0
        self.assertEqual(get_pairs_count(arr, n, sum), 2)

    def test_single_element_array(self):
        arr = [1]
        n = len(arr)
        sum = 2
        self.assertEqual(get_pairs_count(arr, n, sum), 0)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        sum = 1
        self.assertEqual(get_pairs_count(arr, n, sum), 0)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        sum = -3
        self.assertEqual(get_pairs_count(arr, n, sum), 1)
