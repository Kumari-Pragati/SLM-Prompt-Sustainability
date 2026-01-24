import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):

    def test_simple_valid(self):
        self.assertTrue(check_triplet([1, 2, 3], 2, 3, 0))
        self.assertTrue(check_triplet([1, 2, 4], 2, 7, 0))
        self.assertTrue(check_triplet([-1, 0, 1], 2, 0, 0))

    def test_edge_conditions(self):
        self.assertFalse(check_triplet([], 0, 0, 0))
        self.assertFalse(check_triplet([1], 0, 0, 0))
        self.assertFalse(check_triplet([1, 2], 1, 0, 0))
        self.assertFalse(check_triplet([1, 2, 3], 3, 0, 0))
        self.assertFalse(check_triplet([1, 2, 3], 2, 1, 0))
        self.assertFalse(check_triplet([1, 2, 3], 2, 4, 0))
        self.assertFalse(check_triplet([1, 2, 3], 2, -1, 0))

    def test_complex_scenarios(self):
        self.assertTrue(check_triplet([1, 2, 3, -1], 3, 0, 0))
        self.assertTrue(check_triplet([1, 2, -3, -4], 3, 0, 0))
        self.assertFalse(check_triplet([1, 2, 3, 4], 3, 9, 0))
        self.assertFalse(check_triplet([1, 2, 3, -4], 3, -1, 0))
