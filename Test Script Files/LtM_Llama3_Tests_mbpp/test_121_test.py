import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(check_triplet([1, 2, 3], 3, 0, 0))

    def test_edge_count_3(self):
        self.assertTrue(check_triplet([1, 2, 3], 3, 0, 3))

    def test_edge_n_0(self):
        self.assertFalse(check_triplet([], 0, 0, 0))

    def test_edge_sum_negative(self):
        self.assertFalse(check_triplet([1, 2, 3], 3, -1, 0))

    def test_edge_count_0(self):
        self.assertFalse(check_triplet([1, 2, 3], 3, 0, 0))

    def test_edge_n_1(self):
        self.assertFalse(check_triplet([1], 1, 0, 0))

    def test_edge_sum_zero(self):
        self.assertTrue(check_triplet([1, -1, 0], 3, 0, 3))

    def test_edge_count_2(self):
        self.assertFalse(check_triplet([1, 2], 2, 0, 2))

    def test_edge_n_2(self):
        self.assertFalse(check_triplet([1, 2], 2, 0, 0))

    def test_edge_sum_negative_2(self):
        self.assertFalse(check_triplet([1, 2, 3], 3, -2, 0))

    def test_edge_count_1(self):
        self.assertFalse(check_triplet([1], 1, 0, 1))

    def test_edge_n_3(self):
        self.assertFalse(check_triplet([1, 2, 3], 3, 0, 0))

    def test_edge_sum_zero_2(self):
        self.assertTrue(check_triplet([1, -1, 0], 3, 0, 3))

    def test_edge_count_0_2(self):
        self.assertFalse(check_triplet([1, 2], 2, 0, 0))

    def test_edge_n_1_2(self):
        self.assertFalse(check_triplet([1, 2], 2, 0, 0))

    def test_edge_sum_negative_3(self):
        self.assertFalse(check_triplet([1, 2, 3], 3, -3, 0))
