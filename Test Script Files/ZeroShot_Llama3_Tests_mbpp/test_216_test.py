import unittest
from mbpp_216_code import check_subset_list

class TestCheckSubsetList(unittest.TestCase):

    def test_subset_list(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2, 3]))

    def test_subset_list_with_duplicates(self):
        self.assertTrue(check_subset_list([1, 2, 2, 3], [1, 2, 2, 3]))

    def test_subset_list_with_duplicates_and_order_matters(self):
        self.assertFalse(check_subset_list([1, 2, 3], [2, 1, 3]))

    def test_subset_list_with_empty_list(self):
        self.assertTrue(check_subset_list([], []))

    def test_subset_list_with_empty_list2(self):
        self.assertFalse(check_subset_list([1, 2, 3], []))

    def test_subset_list_with_empty_list1(self):
        self.assertFalse(check_subset_list([], [1, 2, 3]))

    def test_subset_list_with_single_element(self):
        self.assertTrue(check_subset_list([1], [1]))

    def test_subset_list_with_single_element2(self):
        self.assertFalse(check_subset_list([1, 2], [1]))

    def test_subset_list_with_single_element3(self):
        self.assertFalse(check_subset_list([1], [2]))

    def test_subset_list_with_multiple_elements(self):
        self.assertTrue(check_subset_list([1, 2, 3], [1, 2]))

    def test_subset_list_with_multiple_elements2(self):
        self.assertFalse(check_subset_list([1, 2, 3], [1, 3]))

    def test_subset_list_with_multiple_elements3(self):
        self.assertFalse(check_subset_list([1, 2, 3], [2, 3]))
