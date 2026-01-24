import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(max_Abs_Diff([-1, -2, -3, -4, -5], 5), 6)
        self.assertEqual(max_Abs_Diff([0, 0, 0, 0, 0], 5), 0)

    def test_edge_cases(self):
        self.assertEqual(max_Abs_Diff([1], 1), 0)
        self.assertEqual(max_Abs_Diff([1, 1], 2), 0)
        self.assertEqual(max_Abs_Diff([-1, 1], 2), 2)
        self.assertEqual(max_Abs_Diff([-1, -1], 2), 2)

    def test_boundary_cases(self):
        self.assertEqual(max_Abs_Diff([-1000000000, -1, 1, 1000000000], 4), 1000000001)
        self.assertEqual(max_Abs_Diff([-1000000000, -1, 1, 1000000000], 1), 1000000000)
        self.assertEqual(max_Abs_Diff([-1000000000, -1, 1, 1000000000], 0), 0)
