import unittest
from mbpp_492_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_found(self):
        item_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(binary_search(item_list, 5))

    def test_not_found(self):
        item_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertFalse(binary_search(item_list, 11))

    def test_empty_list(self):
        item_list = []
        self.assertFalse(binary_search(item_list, 5))

    def test_single_element_list(self):
        item_list = [5]
        self.assertTrue(binary_search(item_list, 5))
        self.assertFalse(binary_search(item_list, 11))

    def test_edge_cases(self):
        item_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(binary_search(item_list, 1))
        self.assertTrue(binary_search(item_list, 10))
