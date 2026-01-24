import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairOrSum(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 28)

    def test_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 0)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 0)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 28)

    def test_large_numbers(self):
        arr = [1000, 2000, 3000, 4000]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 28000)

    def test_duplicate_numbers(self):
        arr = [1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 6)
