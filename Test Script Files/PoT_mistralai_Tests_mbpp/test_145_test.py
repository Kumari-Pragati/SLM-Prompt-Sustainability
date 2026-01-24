import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(max_Abs_Diff([-1, -2, -3, -4, -5], 5), 6)
        self.assertEqual(max_Abs_Diff([0, 0, 0, 0, 0], 5), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_Abs_Diff([1], 1), 0)
        self.assertEqual(max_Abs_Diff([-1], 1), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_Abs_Diff([], 0), 0)

    def test_edge_case_negative_n(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3], -1), TraceError)
