import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3], 3), 2)
        self.assertEqual(max_Abs_Diff([-1, -2, -3], 3), 4)
        self.assertEqual(max_Abs_Diff([0, 0, 0], 3), 0)

    def test_edge_cases(self):
        self.assertEqual(max_Abs_Diff([1], 1), 0)
        self.assertEqual(max_Abs_Diff([-1], 1), 1)
        self.assertEqual(max_Abs_Diff([1, -1], 2), 2)
        self.assertEqual(max_Abs_Diff([-1, -1], 2), 0)

    def test_boundary_conditions(self):
        self.assertEqual(max_Abs_Diff([1000000000], 1), 1000000000)
        self.assertEqual(max_Abs_Diff([-1000000000], 1), 1000000000)

    def test_empty_list(self):
        self.assertEqual(max_Abs_Diff([], 0), 0)

    def test_negative_n(self):
        self.assertEqual(max_Abs_Diff([1], -1), 1)
