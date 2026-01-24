import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_triplet([1, 2, 3], 2, 3, 0))
        self.assertTrue(check_triplet([1, 2, 4], 2, 5, 0))
        self.assertTrue(check_triplet([-1, 0, 1], 2, 0, 0))

    def test_edge_cases(self):
        self.assertFalse(check_triplet([1, 2, 3], 2, 4, 0))
        self.assertFalse(check_triplet([1, 2, 3], 0, 3, 0))
        self.assertFalse(check_triplet([], 0, 3, 0))
        self.assertFalse(check_triplet([1], 0, 1, 0))

    def test_boundary_cases(self):
        self.assertFalse(check_triplet([1, 2, 3], 2, 0, 3))
        self.assertFalse(check_triplet([1, 2, 3], 2, 1, 3))
