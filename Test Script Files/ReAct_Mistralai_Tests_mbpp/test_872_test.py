import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_empty_lists(self):
        self.assertTrue(check_subset([], []))

    def test_single_element_lists(self):
        self.assertTrue(check_subset([1], [1]))
        self.assertFalse(check_subset([1], []))
        self.assertFalse(check_subset([], [1]))

    def test_equal_lists(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3]))

    def test_subset_with_duplicates(self):
        self.assertTrue(check_subset([1, 1, 2, 3], [1, 2, 3]))

    def test_proper_subset(self):
        self.assertTrue(check_subset([1, 2], [1, 2, 3]))

    def test_reverse_subset(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2]))

    def test_non_subset(self):
        self.assertFalse(check_subset([1, 2, 3], [4, 5, 6]))

    def test_list1_in_list2(self):
        self.assertTrue(check_subset(list(range(1, 6)), list(range(1, 10))))

    def test_list2_in_list1(self):
        self.assertTrue(check_subset(list(range(1, 10)), list(range(1, 6))))

    def test_list1_contains_nonexistent_element(self):
        self.assertFalse(check_subset([1, 2, 3], [4, 5, 6, 7]))

    def test_list2_contains_nonexistent_element(self):
        self.assertFalse(check_subset([1, 2, 3], [1, 2, 9]))
