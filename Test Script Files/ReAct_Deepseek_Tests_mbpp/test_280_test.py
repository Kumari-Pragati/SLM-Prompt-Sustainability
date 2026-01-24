import unittest
from mbpp_280_code import sequential_search

class TestSequentialSearch(unittest.TestCase):

    def test_typical_case(self):
        data_list = [1, 2, 3, 4, 5]
        item = 3
        result, position = sequential_search(data_list, item)
        self.assertTrue(result)
        self.assertEqual(position, 2)

    def test_item_not_in_list(self):
        data_list = [1, 2, 3, 4, 5]
        item = 6
        result, position = sequential_search(data_list, item)
        self.assertFalse(result)
        self.assertEqual(position, 5)

    def test_empty_list(self):
        data_list = []
        item = 1
        result, position = sequential_search(data_list, item)
        self.assertFalse(result)
        self.assertEqual(position, 0)

    def test_list_with_duplicates(self):
        data_list = [1, 2, 3, 2, 5]
        item = 2
        result, position = sequential_search(data_list, item)
        self.assertTrue(result)
        self.assertEqual(position, 1)  # First occurrence

    def test_single_item_list(self):
        data_list = [1]
        item = 1
        result, position = sequential_search(data_list, item)
        self.assertTrue(result)
        self.assertEqual(position, 0)
