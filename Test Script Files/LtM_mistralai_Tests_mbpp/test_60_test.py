import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_len_sub([1, 2, 3, 2, 1], 5), 3)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(max_len_sub([5, 4, 3, 2, 1], 5), 1)

    def test_edge_cases(self):
        self.assertEqual(max_len_sub([1, 1, 1, 1, 1], 5), 1)
        self.assertEqual(max_len_sub([1, 2, 3, 4, 5], 1), 1)
        self.assertEqual(max_len_sub([], 0), 0)
        self.assertEqual(max_len_sub([1], 1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(max_len_sub([-100, -99, -98, -97, -96], 5), 1)
        self.assertEqual(max_len_sub([99, 100, 101, 102, 103], 5), 5)
        self.assertEqual(max_len_sub([0, 0, 0, 0, 0], 5), 1)

    def test_complex_cases(self):
        self.assertEqual(max_len_sub([1, 2, 1, 3, 2, 1, 4, 3, 2, 1], 10), 4)
        self.assertEqual(max_len_sub([1, 2, 1, 0, 3, 2, 1, -1, 4, 3, 2, 1], 12), 4)
