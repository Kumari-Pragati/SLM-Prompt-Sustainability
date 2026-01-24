import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Ops([1, 2, 3, 4], 4, 1), 2)
        self.assertEqual(min_Ops([1, 2, 3, 4], 4, 2), 1)
        self.assertEqual(min_Ops([1, 2, 3, 4], 4, 3), 0)

    def test_edge_case_k_is_1(self):
        self.assertEqual(min_Ops([1, 2, 3, 4], 4, 0), -1)
        self.assertEqual(min_Ops([1, 2, 3, 4], 1, 1), -1)
        self.assertEqual(min_Ops([1, 2, 3, 4], 2, 1), -1)

    def test_edge_case_n_is_1(self):
        self.assertEqual(min_Ops([1], 1, 1), 0)
        self.assertEqual(min_Ops([1], 1, 2), -1)

    def test_corner_case_arr_is_sorted(self):
        self.assertEqual(min_Ops([1, 2, 3, 4], 4, 1), 2)
        self.assertEqual(min_Ops([1, 1, 1, 1], 4, 1), 0)

    def test_corner_case_arr_is_reverse_sorted(self):
        self.assertEqual(min_Ops([4, 3, 2, 1], 4, 1), 2)
        self.assertEqual(min_Ops([4, 4, 4, 4], 4, 1), 0)
