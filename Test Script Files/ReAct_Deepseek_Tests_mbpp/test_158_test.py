import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):

    def test_typical_case(self):
        arr = [10, 20, 30]
        n = len(arr)
        k = 10
        self.assertEqual(min_Ops(arr, n, k), 3)

    def test_edge_case_with_single_element(self):
        arr = [5]
        n = len(arr)
        k = 5
        self.assertEqual(min_Ops(arr, n, k), 1)

    def test_edge_case_with_same_elements(self):
        arr = [5, 5, 5]
        n = len(arr)
        k = 5
        self.assertEqual(min_Ops(arr, n, k), 3)

    def test_edge_case_with_k_greater_than_max_difference(self):
        arr = [1, 2, 3]
        n = len(arr)
        k = 1
        self.assertEqual(min_Ops(arr, n, k), -1)

    def test_edge_case_with_k_equal_to_zero(self):
        arr = [1, 2, 3]
        n = len(arr)
        k = 0
        self.assertEqual(min_Ops(arr, n, k), -1)

    def test_error_case_with_negative_elements(self):
        arr = [10, -20, 30]
        n = len(arr)
        k = 10
        self.assertEqual(min_Ops(arr, n, k), -1)
