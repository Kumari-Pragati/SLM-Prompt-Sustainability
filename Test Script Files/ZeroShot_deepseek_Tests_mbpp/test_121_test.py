import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):

    def test_positive_numbers(self):
        A = [1, 2, 3, 4, 5]
        self.assertTrue(check_triplet(A, len(A), 6, 0))

    def test_negative_numbers(self):
        A = [-1, -2, -3, -4, -5]
        self.assertFalse(check_triplet(A, len(A), -6, 0))

    def test_mixed_numbers(self):
        A = [1, -2, 3, -4, 5]
        self.assertFalse(check_triplet(A, len(A), 0, 0))

    def test_empty_list(self):
        A = []
        self.assertFalse(check_triplet(A, len(A), 0, 0))

    def test_sum_not_zero(self):
        A = [1, 2, 3, 4, 5]
        self.assertFalse(check_triplet(A, len(A), 10, 0))

    def test_count_not_three(self):
        A = [1, 2, 3, 4, 5]
        self.assertFalse(check_triplet(A, len(A), 6, 2))
