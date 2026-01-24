import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 2), [3, 4, 5, 1, 2])

    def test_edge_case_empty_array(self):
        self.assertEqual(split_Arr([], 0, 0), [])

    def test_edge_case_k_equals_n(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 5), [1, 2, 3, 4, 5])

    def test_edge_case_k_greater_than_n(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, 6), [2, 3, 4, 5, 1])

    def test_edge_case_k_less_than_0(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 5, -1), [1, 2, 3, 4, 5])

    def test_complex_case_large_array(self):
        self.assertEqual(split_Arr(list(range(1, 101)), 100, 50), list(range(51, 101)) + list(range(1, 51)))
