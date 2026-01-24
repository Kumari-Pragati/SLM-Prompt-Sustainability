import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNumbs(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(rearrange_numbs([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_zero_in_array(self):
        self.assertEqual(rearrange_numbs([0, 1, 2, 3, 4]), [0, 4, 3, 2, 1])

    def test_negative_numbers(self):
        self.assertEqual(rearrange_numbs([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])

    def test_positive_and_negative_numbers(self):
        self.assertEqual(rearrange_numbs([1, -1, 2, -2, 3, -3]), [3, -3, 2, -2, 1, -1])

    def test_zero_and_negative_numbers(self):
        self.assertEqual(rearrange_numbs([0, -1, -2, -3, -4]), [0, -4, -3, -2, -1])

    def test_zero_and_positive_numbers(self):
        self.assertEqual(rearrange_numbs([0, 1, 2, 3, 4]), [0, 4, 3, 2, 1])

    def test_edge_case_empty_array(self):
        self.assertEqual(rearrange_numbs([]), [])

    def test_edge_case_single_element_array(self):
        self.assertEqual(rearrange_numbs([1]), [1])

    def test_edge_case_array_with_duplicates(self):
        self.assertEqual(rearrange_numbs([1, 2, 2, 3, 3, 3]), [3, 3, 3, 2, 2, 1])
