import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case_min_max_equal(self):
        self.assertEqual(max_Abs_Diff([1, 1, 1, 1, 1], 5), 0)

    def test_edge_case_min_max_diff(self):
        self.assertEqual(max_Abs_Diff([-1, 1, 2, 3, 4], 5), 4)

    def test_edge_case_single_element(self):
        self.assertEqual(max_Abs_Diff([1], 1), 0)

    def test_edge_case_empty_array(self):
        with self.assertRaises(IndexError):
            max_Abs_Diff([], 0)

    def test_edge_case_array_with_one_element(self):
        with self.assertRaises(IndexError):
            max_Abs_Diff([1], 0)

    def test_edge_case_array_with_two_elements(self):
        self.assertEqual(max_Abs_Diff([1, 2], 2), 1)
