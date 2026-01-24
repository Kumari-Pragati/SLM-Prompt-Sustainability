import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(check_triplet([], len([0, 1, 2]), 0, 0))

    def test_single_element(self):
        self.assertFalse(check_triplet([0], len([0, 1, 2]), 0, 0))

    def test_two_elements_sum_zero(self):
        self.assertTrue(check_triplet([0, 0], len([0, 1, 2]), 0, 0))

    def test_two_elements_sum_non_zero(self):
        self.assertFalse(check_triplet([0, 1], len([0, 1, 2]), 0, 0))

    def test_three_elements_sum_zero(self):
        self.assertTrue(check_triplet([0, 1, -1], len([0, 1, 2]), 0, 0))

    def test_three_elements_sum_non_zero(self):
        self.assertFalse(check_triplet([0, 1, 2], len([0, 1, 2]), 0, 0))

    def test_four_elements_sum_zero(self):
        self.assertTrue(check_triplet([0, 1, -1, 2], len([0, 1, 2]), 0, 0))

    def test_four_elements_sum_non_zero(self):
        self.assertFalse(check_triplet([0, 1, 2, 3], len([0, 1, 2]), 0, 0))
