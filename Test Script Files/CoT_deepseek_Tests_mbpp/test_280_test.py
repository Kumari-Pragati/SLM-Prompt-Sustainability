import unittest
from mbpp_280_code import sequential_search

class TestSequentialSearch(unittest.TestCase):

    def test_typical_case(self):
        data_list = [1, 2, 3, 4, 5]
        item = 3
        self.assertEqual(sequential_search(data_list, item), (True, 2))

    def test_item_not_in_list(self):
        data_list = [1, 2, 3, 4, 5]
        item = 6
        self.assertEqual(sequential_search(data_list, item), (False, 5))

    def test_empty_list(self):
        data_list = []
        item = 1
        self.assertEqual(sequential_search(data_list, item), (False, 0))

    def test_list_with_duplicates(self):
        data_list = [1, 2, 3, 2, 5]
        item = 2
        self.assertEqual(sequential_search(data_list, item), (True, 1))

    def test_item_at_beginning(self):
        data_list = [1, 2, 3, 4, 5]
        item = 1
        self.assertEqual(sequential_search(data_list, item), (True, 0))

    def test_item_at_end(self):
        data_list = [1, 2, 3, 4, 5]
        item = 5
        self.assertEqual(sequential_search(data_list, item), (True, 4))

    def test_large_list(self):
        data_list = list(range(1, 10001))
        item = 5000
        self.assertEqual(sequential_search(data_list, item), (True, 4999))
