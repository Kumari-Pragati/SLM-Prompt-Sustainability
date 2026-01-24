import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4], 4), 3)
        self.assertEqual(max_Abs_Diff([-1, -2, -3, -4], 4), 3)
        self.assertEqual(max_Abs_Diff([10, 20, 30, 40], 4), 30)

    def test_edge_conditions(self):
        self.assertEqual(max_Abs_Diff([1], 1), 0)
        self.assertEqual(max_Abs_Diff([], 0), None)

    def test_boundary_conditions(self):
        self.assertEqual(max_Abs_Diff([-1000000000, 1000000000], 2), 2000000000)
        self.assertEqual(max_Abs_Diff([1000000000, -1000000000], 2), 2000000000)

    def test_complex_cases(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5, 6], 6), 5)
        self.assertEqual(max_Abs_Diff([-1, -2, -3, -4, -5, -6], 6), 5)
        self.assertEqual(max_Abs_Diff([-1, 2, -3, 4, -5, 6], 6), 7)
