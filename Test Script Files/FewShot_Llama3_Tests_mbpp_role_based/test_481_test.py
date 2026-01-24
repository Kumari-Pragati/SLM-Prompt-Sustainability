import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):
    def test_subset_sum_true(self):
        set = [3, 34, 4, 12, 5, 2]
        n = len(set)
        sum = 9
        self.assertTrue(is_subset_sum(set, n, sum))

    def test_subset_sum_false(self):
        set = [3, 34, 4, 12, 5, 2]
        n = len(set)
        sum = 10
        self.assertFalse(is_subset_sum(set, n, sum))

    def test_subset_sum_zero(self):
        set = [3, 34, 4, 12, 5, 2]
        n = len(set)
        sum = 0
        self.assertTrue(is_subset_sum(set, n, sum))

    def test_subset_sum_negative(self):
        set = [3, 34, 4, 12, 5, 2]
        n = len(set)
        sum = -1
        self.assertFalse(is_subset_sum(set, n, sum))

    def test_subset_sum_empty_set(self):
        set = []
        n = len(set)
        sum = 5
        self.assertFalse(is_subset_sum(set, n, sum))

    def test_subset_sum_single_element_set(self):
        set = [5]
        n = len(set)
        sum = 5
        self.assertTrue(is_subset_sum(set, n, sum))
