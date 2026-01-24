import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNumbs(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rearrange_numbs([3, 1, 2, 0, 4]), [0, 2, 4, 1, 3])

    def test_edge_case_zero(self):
        self.assertEqual(rearrange_numbs([0, 1, 2, 3, 4]), [0, 4, 3, 2, 1])

    def test_edge_case_negative(self):
        self.assertEqual(rearrange_numbs([-1, -2, -3, 0, 4]), [0, 4, -3, -2, -1])

    def test_edge_case_all_positive(self):
        self.assertEqual(rearrange_numbs([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_edge_case_all_negative(self):
        self.assertEqual(rearrange_numbs([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            rearrange_numbs("Invalid input")

    def test_invalid_input_empty_list(self):
        with self.assertRaises(IndexError):
            rearrange_numbs([])
