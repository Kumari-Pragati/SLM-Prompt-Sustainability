import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_found_in_middle(self):
        item_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(binary_search(item_list, 5))

    def test_found_at_start(self):
        item_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(binary_search(item_list, 1))

    def test_found_at_end(self):
        item_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(binary_search(item_list, 10))

    def test_not_found(self):
        item_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertFalse(binary_search(item_list, 11))

    def test_empty_list(self):
        item_list = []
        self.assertFalse(binary_search(item_list, 1))

    def test_single_element_list(self):
        item_list = [1]
        self.assertTrue(binary_search(item_list, 1))

    def test_list_with_duplicates(self):
        item_list = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(binary_search(item_list, 2))

    def test_list_with_duplicates_and_not_found(self):
        item_list = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertFalse(binary_search(item_list, 11))
