import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_empty_sets(self):
        self.assertFalse(check_subset((), (1, 2, 3)))
        self.assertTrue(check_subset((1, 2, 3), ()))

    def test_equal_sets(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3)))

    def test_subset_case1(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3, 4)))

    def test_subset_case2(self):
        self.assertTrue(check_subset((1, 2), (1, 2, 3)))

    def test_subset_case3(self):
        self.assertFalse(check_subset((1, 2, 3), (1, 2, 4)))

    def test_subset_case4(self):
        self.assertFalse(check_subset((1, 2), (1, 3)))
