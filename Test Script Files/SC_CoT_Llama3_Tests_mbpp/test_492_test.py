import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_found_item(self):
        item_list = [1, 2, 3, 4, 5]
        item = 3
        self.assertTrue(binary_search(item_list, item))

    def test_not_found_item(self):
        item_list = [1, 2, 3, 4, 5]
        item = 6
        self.assertFalse(binary_search(item_list, item))

    def test_edge_case_found_item(self):
        item_list = [1, 2, 3, 4, 5]
        item = 1
        self.assertTrue(binary_search(item_list, item))

    def test_edge_case_not_found_item(self):
        item_list = [1, 2, 3, 4, 5]
        item = 6
        self.assertFalse(binary_search(item_list, item))

    def test_empty_list(self):
        item_list = []
        item = 1
        self.assertFalse(binary_search(item_list, item))

    def test_single_element_list(self):
        item_list = [1]
        item = 1
        self.assertTrue(binary_search(item_list, item))

    def test_single_element_list_not_found(self):
        item_list = [1]
        item = 2
        self.assertFalse(binary_search(item_list, item))

    def test_binary_search_on_sorted_list(self):
        item_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        item = 5
        self.assertTrue(binary_search(item_list, item))

    def test_binary_search_on_unsorted_list(self):
        item_list = [5, 1, 3, 4, 2, 6, 7, 8, 9, 10]
        item = 5
        self.assertTrue(binary_search(item_list, item))

    def test_binary_search_on_duplicates(self):
        item_list = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
        item = 2
        self.assertTrue(binary_search(item_list, item))

    def test_binary_search_on_duplicates_not_found(self):
        item_list = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
        item = 11
        self.assertFalse(binary_search(item_list, item))
