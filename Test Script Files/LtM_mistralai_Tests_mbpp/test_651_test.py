import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_simple_subset(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2)))
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3)))
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3, 4)))

    def test_empty_sets(self):
        self.assertFalse(check_subset((), (1, 2)))
        self.assertTrue(check_subset((1, 2), ()))

    def test_edge_cases(self):
        self.assertTrue(check_subset((1, 2), (1, 2, None)))
        self.assertFalse(check_subset((1, 2), (3, 4)))
        self.assertFalse(check_subset((1, 2), (1, 3)))

    def test_complex_cases(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3, 1)))
        self.assertFalse(check_subset((1, 2, 3), (3, 2, 1)))
        self.assertFalse(check_subset((1, 2, 3), (3, 4, 5)))
