import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):
    def test_typical_use_case(self):
        items = [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 5}, {'name': 'item3', 'price': 15}, {'name': 'item4', 'price': 2}]
        expected = [{'name': 'item2', 'price': 5}, {'name': 'item4', 'price': 2}]
        self.assertEqual(cheap_items(items, 2), expected)

    def test_empty_list(self):
        self.assertRaises(IndexError, cheap_items, [], 1)

    def test_single_item(self):
        items = [{'name': 'item1', 'price': 10}]
        expected = [{'name': 'item1', 'price': 10}]
        self.assertEqual(cheap_items(items, 1), expected)

    def test_negative_n(self):
        self.assertRaises(ValueError, cheap_items, [{'name': 'item1', 'price': 10}], -1)
