import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairORSum(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 28)

    def test_empty_array(self):
        arr = []
        n = 0
        self.assertEqual(pair_OR_Sum(arr, n), 0)

    def test_single_element_array(self):
        arr = [5]
        n = 1
        self.assertEqual(pair_OR_Sum(arr, n), 0)

    def test_duplicate_elements(self):
        arr = [2, 2, 2, 2]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 0)

    def test_large_numbers(self):
        arr = [1000, 2000, 3000, 4000]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 28000)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), -28)

    def test_mixed_numbers(self):
        arr = [-1, 2, -3, 4]
        n = len(arr)
        self.assertEqual(pair_OR_Sum(arr, n), 12)
