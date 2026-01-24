import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_triplet([1, 2, 3], 3, 0, 0))

    def test_edge_case_sum_zero(self):
        self.assertTrue(check_triplet([1, -1, 1], 3, 0, 0))

    def test_edge_case_count_three(self):
        self.assertTrue(check_triplet([1, 2, 3], 3, 0, 3))

    def test_edge_case_n_zero(self):
        self.assertFalse(check_triplet([1, 2, 3], 0, 0, 0))

    def test_edge_case_sum_negative(self):
        self.assertFalse(check_triplet([1, 2, 3], 3, -1, 0))

    def test_edge_case_count_zero(self):
        self.assertFalse(check_triplet([1, 2, 3], 3, 0, 0))

    def test_edge_case_n_one(self):
        self.assertFalse(check_triplet([1], 1, 0, 0))

    def test_edge_case_sum_one(self):
        self.assertFalse(check_triplet([1, 2, 3], 3, 1, 0))

    def test_edge_case_count_two(self):
        self.assertFalse(check_triplet([1, 2, 3], 3, 0, 2))

    def test_edge_case_n_two(self):
        self.assertFalse(check_triplet([1, 2], 2, 0, 0))

    def test_edge_case_sum_two(self):
        self.assertFalse(check_triplet([1, 2, 3], 3, 2, 0))
