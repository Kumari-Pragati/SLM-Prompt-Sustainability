import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):
    def test_typical_use_case(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 10
        k = 2
        self.assertEqual(max_sub_array_sum_repeated(a, n, k), 18)

    def test_edge_case_negative_numbers(self):
        a = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        n = 10
        k = 2
        self.assertEqual(max_sub_array_sum_repeated(a, n, k), -6)

    def test_edge_case_zero_sum(self):
        a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        n = 10
        k = 2
        self.assertEqual(max_sub_array_sum_repeated(a, n, k), 0)

    def test_edge_case_single_element_array(self):
        a = [5]
        n = 1
        k = 1
        self.assertEqual(max_sub_array_sum_repeated(a, n, k), 5)

    def test_edge_case_empty_array(self):
        a = []
        n = 0
        k = 1
        self.assertEqual(max_sub_array_sum_repeated(a, n, k), -2147483648)
