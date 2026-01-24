import unittest
from mbpp_144_code import sum_Pairs

class TestSumPairs(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(sum_Pairs(arr, n), 10)

    def test_edge_case_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(sum_Pairs(arr, n), 0)

    def test_boundary_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(sum_Pairs(arr, n), 0)

    def test_corner_case_negative_elements(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(sum_Pairs(arr, n), -10)

    def test_corner_case_large_numbers(self):
        arr = [1000, 2000, 3000, 4000, 5000]
        n = len(arr)
        self.assertEqual(sum_Pairs(arr, n), 10000)

    def test_corner_case_large_n(self):
        arr = [1, 2, 3, 4, 5]
        n = 10000
        self.assertEqual(sum_Pairs(arr, n), 10)
