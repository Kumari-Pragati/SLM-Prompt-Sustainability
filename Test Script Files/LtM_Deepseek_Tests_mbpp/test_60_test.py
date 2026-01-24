import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4], 4), 4)
        self.assertEqual(max_len_sub([1, 1, 1, 1], 4), 4)
        self.assertEqual(max_len_sub([10, 22, 9, 33, 21, 50, 41, 60, 80], 9), 6)

    def test_edge_conditions(self):
        self.assertEqual(max_len_sub([], 0), 0)
        self.assertEqual(max_len_sub([1], 1), 1)
        self.assertEqual(max_len_sub([1, 2], 2), 2)

    def test_boundary_conditions(self):
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(max_len_sub([5, 4, 3, 2, 1], 5), 5)
        self.assertEqual(max_len_sub([1, 3, 5, 7, 9], 5), 1)

    def test_complex_cases(self):
        self.assertEqual(max_len_sub([10, 22, 9, 33, 21, 50, 41, 60, 80], 9), 6)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 4, 3, 2, 1], 9), 9)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 9)
