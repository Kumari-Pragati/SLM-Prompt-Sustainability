import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [10, 20, 30, 40]
        n = len(arr)
        k = 10
        self.assertEqual(min_Ops(arr, n, k), 6)

    def test_edge_case_max_equals_min(self):
        arr = [10, 10, 10, 10]
        n = len(arr)
        k = 10
        self.assertEqual(min_Ops(arr, n, k), 0)

    def test_boundary_condition_max_greater_than_min(self):
        arr = [1, 2, 3, 4]
        n = len(arr)
        k = 2
        self.assertEqual(min_Ops(arr, n, k), 6)

    def test_boundary_condition_max_less_than_min(self):
        arr = [4, 3, 2, 1]
        n = len(arr)
        k = 2
        self.assertEqual(min_Ops(arr, n, k), -1)

    def test_invalid_input_negative_numbers(self):
        arr = [-1, -2, -3, -4]
        n = len(arr)
        k = 2
        self.assertEqual(min_Ops(arr, n, k), -1)

    def test_invalid_input_non_integer_numbers(self):
        arr = [1.5, 2.5, 3.5, 4.5]
        n = len(arr)
        k = 2
        self.assertEqual(min_Ops(arr, n, k), -1)

    def test_invalid_input_k_equals_zero(self):
        arr = [1, 2, 3, 4]
        n = len(arr)
        k = 0
        self.assertEqual(min_Ops(arr, n, k), -1)
