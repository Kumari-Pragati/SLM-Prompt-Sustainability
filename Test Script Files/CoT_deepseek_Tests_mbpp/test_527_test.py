import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 10, 0]
        n = len(arr)
        sum = 10
        self.assertEqual(get_pairs_count(arr, n, sum), 6)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        sum = 10
        self.assertEqual(get_pairs_count(arr, n, sum), 0)

    def test_single_element(self):
        arr = [5]
        n = len(arr)
        sum = 10
        self.assertEqual(get_pairs_count(arr, n, sum), 0)

    def test_sum_not_present(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 10
        self.assertEqual(get_pairs_count(arr, n, sum), 0)

    def test_sum_present(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 5
        self.assertEqual(get_pairs_count(arr, n, sum), 2)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        sum = -6
        self.assertEqual(get_pairs_count(arr, n, sum), 2)

    def test_large_numbers(self):
        arr = [1000, 2000, 3000, 4000, 5000]
        n = len(arr)
        sum = 6000
        self.assertEqual(get_pairs_count(arr, n, sum), 2)
