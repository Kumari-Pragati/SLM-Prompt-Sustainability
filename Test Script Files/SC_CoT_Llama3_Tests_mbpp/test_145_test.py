import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case_min_max_equal(self):
        self.assertEqual(max_Abs_Diff([1, 1, 1, 1, 1], 5), 0)

    def test_edge_case_min_max_zero(self):
        self.assertEqual(max_Abs_Diff([0, 0, 0, 0, 0], 5), 0)

    def test_edge_case_min_max_negative(self):
        self.assertEqual(max_Abs_Diff([-1, -2, -3, -4, -5], 5), 4)

    def test_edge_case_min_max_positive(self):
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case_min_max_negative_zero(self):
        self.assertEqual(max_Abs_Diff([-1, 0, 1, -2, 2], 5), 2)

    def test_edge_case_min_max_positive_zero(self):
        self.assertEqual(max_Abs_Diff([1, 0, -1, 2, -2], 5), 2)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            max_Abs_Diff([1, 2, 3, 4, 5.5], 5)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            max_Abs_Diff("hello", 5)

    def test_invalid_input_non_positive_length(self):
        with self.assertRaises(TypeError):
            max_Abs_Diff([1, 2, 3], 0)

    def test_invalid_input_non_positive_length_negative(self):
        with self.assertRaises(TypeError):
            max_Abs_Diff([1, 2, 3], -5)
