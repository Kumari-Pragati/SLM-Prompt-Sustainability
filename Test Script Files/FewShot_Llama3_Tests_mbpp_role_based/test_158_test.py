import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        k = 2
        self.assertEqual(min_Ops(arr, n, k), 2)

    def test_edge_case_max_in_array(self):
        arr = [10, 20, 30, 40, 50]
        n = 5
        k = 2
        self.assertEqual(min_Ops(arr, n, k), 2)

    def test_edge_case_min_in_array(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        k = 2
        self.assertEqual(min_Ops(arr, n, k), 2)

    def test_edge_case_k_is_zero(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        k = 0
        self.assertEqual(min_Ops(arr, n, k), -1)

    def test_edge_case_k_is_one(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        k = 1
        self.assertEqual(min_Ops(arr, n, k), 2)

    def test_invalid_input_negative_k(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        k = -1
        self.assertEqual(min_Ops(arr, n, k), -1)

    def test_invalid_input_negative_n(self):
        arr = [1, 2, 3, 4, 5]
        n = -1
        k = 2
        self.assertEqual(min_Ops(arr, n, k), -1)
