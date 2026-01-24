import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(cheap_items([], 5), [])

    def test_single_item(self):
        items = [{'price': 10}]
        self.assertEqual(cheap_items(items, 1), [{'price': 10}])

    def test_multiple_items(self):
        items = [{'price': 10}, {'price': 5}, {'price': 8}, {'price': 3}, {'price': 7}]
        self.assertEqual(cheap_items(items, 3), sorted([{'price': 3}, {'price': 5}, {'price': 7}], key=lambda s: s['price']))

    def test_n_is_greater_than_items(self):
        items = [{'price': 10}, {'price': 5}, {'price': 8}, {'price': 3}, {'price': 7}]
        self.assertEqual(cheap_items(items, 10), sorted([{'price': 3}, {'price': 5}, {'price': 7}, {'price': 8}, {'price': 10}], key=lambda s: s['price']))
