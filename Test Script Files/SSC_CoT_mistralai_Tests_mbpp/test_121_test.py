import unittest
from mbpp_121_code import check_triplet

class TestCheckTriplet(unittest.TestCase):

    def test_normal(self):
        self.assertTrue(check_triplet([1, 2, 3], 2, 6, 1))
        self.assertTrue(check_triplet([1, 2, 3], 2, 3, 1))
        self.assertTrue(check_triplet([1, 2, 3], 2, 4, 1))
        self.assertTrue(check_triplet([1, 2, 3], 1, 2, 1))
        self.assertTrue(check_triplet([1, 2, 3], 1, 3, 1))
        self.assertTrue(check_triplet([1, 2, 3], 1, 4, 2))
        self.assertTrue(check_triplet([1, 2, 3], 0, 1, 1))
        self.assertTrue(check_triplet([1, 2, 3], 0, 2, 1))
        self.assertTrue(check_triplet([1, 2, 3], 0, 3, 1))
        self.assertTrue(check_triplet([1, 2, 3], 0, 4, 2))

    def test_edge_cases(self):
        self.assertFalse(check_triplet([1, 2, 3], 3, 6, 3))
        self.assertFalse(check_triplet([1, 2, 3], 2, 7, 1))
        self.assertFalse(check_triplet([1, 2, 3], 2, -1, 1))
        self.assertFalse(check_triplet([1, 2, 3], 2, 0, 4))
        self.assertFalse(check_triplet([1, 2, 3], -1, 6, 1))
        self.assertFalse(check_triplet([1, 2, 3], 0, -1, 1))
