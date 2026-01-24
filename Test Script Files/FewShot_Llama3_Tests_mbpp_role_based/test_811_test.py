import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):
    def test_identical_lists(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        self.assertTrue(check_identical(list1, list2))

    def test_non_identical_lists(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 4]
        self.assertFalse(check_identical(list1, list2))

    def test_empty_lists(self):
        list1 = []
        list2 = []
        self.assertTrue(check_identical(list1, list2))

    def test_empty_list_and_non_empty_list(self):
        list1 = []
        list2 = [1, 2, 3]
        self.assertFalse(check_identical(list1, list2))

    def test_lists_with_same_elements_in_different_order(self):
        list1 = [1, 2, 3]
        list2 = [3, 2, 1]
        self.assertTrue(check_identical(list1, list2))
