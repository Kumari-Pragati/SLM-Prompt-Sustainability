import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_Abs_Diff([1, 3, 9, 7, 5], 5), 8)

    def test_edge_case_single_element(self):
        self.assertEqual(max_Abs_Diff([5], 1), 0)

    def test_boundary_case_empty_array(self):
        self.assertEqual(max_Abs_Diff([], 0), None)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(max_Abs_Diff([-1, -3, -9, -7, -5], 5), 8)

    def test_corner_case_mixed_numbers(self):
        self.assertEqual(max_Abs_Diff([-1, 3, -9, 7, -5], 5), 16)
