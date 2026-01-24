import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):

    def test_simple_case(self):
        self.assertTrue(check_triplet([-1, 0, 1, 2, -1, -4], 6, 0, 0))

    def test_edge_case_empty_array(self):
        self.assertFalse(check_triplet([], 0, 0, 0))

    def test_edge_case_sum_zero_with_one_element(self):
        self.assertFalse(check_triplet([0], 1, 0, 0))

    def test_edge_case_sum_zero_with_two_elements(self):
        self.assertFalse(check_triplet([0, 0], 2, 0, 0))

    def test_edge_case_sum_zero_with_three_elements(self):
        self.assertTrue(check_triplet([0, 0, 0], 3, 0, 0))

    def test_boundary_case_max_values(self):
        self.assertFalse(check_triplet([1000, 1000, 1000, 1000], 4, 3000, 0))

    def test_complex_case_negative_numbers(self):
        self.assertTrue(check_triplet([-2, -1, 0, 1, 2], 5, 0, 0))

    def test_complex_case_mixed_numbers(self):
        self.assertFalse(check_triplet([-1, 0, 1, 2, -1, -4], 6, 1, 0))
