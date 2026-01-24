import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):

    def test_typical_case(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        n = len(a)
        k = 3
        expected_output = [4, 5, 6, 7, 8, 9, 1, 2, 3]
        self.assertEqual(split_Arr(a, n, k), expected_output)

    def test_edge_case_k_equals_n(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        k = n
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(split_Arr(a, n, k), expected_output)

    def test_edge_case_k_equals_0(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        k = 0
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(split_Arr(a, n, k), expected_output)

    def test_edge_case_k_greater_than_n(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        k = n + 1
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(split_Arr(a, n, k), expected_output)

    def test_error_case_negative_k(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        k = -1
        with self.assertRaises(IndexError):
            split_Arr(a, n, k)
