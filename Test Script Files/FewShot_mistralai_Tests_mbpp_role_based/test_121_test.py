import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):
    def test_valid_triplet(self):
        self.assertTrue(check_triplet([1, 2, 3], 2, 6, 0))
        self.assertTrue(check_triplet([1, 2, 4], 2, 7, 0))
        self.assertTrue(check_triplet([-1, 0, 1], 2, 0, 0))

    def test_invalid_input_count(self):
        self.assertFalse(check_triplet([1, 2, 3], 4, 6, 0))

    def test_invalid_input_sum(self):
        self.assertFalse(check_triplet([1, 2, 3], 2, 7, 0))

    def test_invalid_input_array(self):
        self.assertFalse(check_triplet([], 2, 6, 0))
        self.assertFalse(check_triplet([1], 1, 6, 0))
