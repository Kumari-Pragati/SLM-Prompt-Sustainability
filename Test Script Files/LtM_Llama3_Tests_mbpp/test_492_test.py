import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_found_item(self):
        item_list = [1, 2, 3, 4, 5]
        self.assertTrue(binary_search(item_list, 3))

    def test_not_found_item(self):
        item_list = [1, 2, 3, 4, 5]
        self.assertFalse(binary_search(item_list, 6))

    def test_empty_list(self):
        item_list = []
        self.assertFalse(binary_search(item_list, 1))

    def test_single_element_list(self):
        item_list = [1]
        self.assertTrue(binary_search(item_list, 1))
        self.assertFalse(binary_search(item_list, 2))

    def test_edge_cases(self):
        item_list = [1, 2, 3, 4, 5]
        self.assertTrue(binary_search(item_list, 1))
        self.assertTrue(binary_search(item_list, 5))

    def test_large_list(self):
        item_list = list(range(1000))
        self.assertTrue(binary_search(item_list, 500))

    def test_duplicates(self):
        item_list = [1, 2, 2, 3, 4, 5]
        self.assertTrue(binary_search(item_list, 2))
