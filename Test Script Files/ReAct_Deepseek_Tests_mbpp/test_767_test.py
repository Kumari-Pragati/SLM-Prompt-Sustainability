import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 10, 0]
        n = len(arr)
        sum = 10
        self.assertEqual(get_Pairs_Count(arr, n, sum), 6)

    def test_empty_array(self):
        arr = []
        n = 0
        sum = 10
        self.assertEqual(get_Pairs_Count(arr, n, sum), 0)

    def test_single_element(self):
        arr = [5]
        n = 1
        sum = 10
        self.assertEqual(get_Pairs_Count(arr, n, sum), 0)

    def test_no_pairs(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 10
        self.assertEqual(get_Pairs_Count(arr, n, sum), 0)

    def test_negative_numbers(self):
        arr = [-1, -9, 2, 8, 3, 7, -4, 6, 5, 5, 10, 0]
        n = len(arr)
        sum = 10
        self.assertEqual(get_Pairs_Count(arr, n, sum), 6)

    def test_large_array(self):
        arr = list(range(1, 1001))
        n = len(arr)
        sum = 1000
        self.assertEqual(get_Pairs_Count(arr, n, sum), 499500)
