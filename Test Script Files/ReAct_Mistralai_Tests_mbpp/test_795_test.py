import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            cheap_items([], 1)

    def test_single_item(self):
        item = {'name': 'Item 1', 'price': 10}
        result = cheap_items([item], 1)
        self.assertEqual(result, [item])

    def test_multiple_items_one_cheapest(self):
        item1 = {'name': 'Item 1', 'price': 10}
        item2 = {'name': 'Item 2', 'price': 11}
        items = [item1, item2]
        result = cheap_items(items, 1)
        self.assertEqual(result, [item1])

    def test_multiple_items_multiple_cheapest(self):
        item1 = {'name': 'Item 1', 'price': 10}
        item2 = {'name': 'Item 2', 'price': 10}
        item3 = {'name': 'Item 3', 'price': 12}
        items = [item1, item2, item3]
        result = cheap_items(items, 2)
        self.assertEqual(result, [item1, item2])

    def test_multiple_items_one_more_than_n(self):
        item1 = {'name': 'Item 1', 'price': 10}
        item2 = {'name': 'Item 2', 'price': 11}
        item3 = {'name': 'Item 3', 'price': 12}
        items = [item1, item2, item3]
        with self.assertRaises(ValueError):
            cheap_items(items, 2)

    def test_items_with_same_price(self):
        item1 = {'name': 'Item 1', 'price': 10}
        item2 = {'name': 'Item 2', 'price': 10}
        item3 = {'name': 'Item 3', 'price': 12}
        items = [item1, item2, item3]
        result = cheap_items(items, 2)
        self.assertEqual(result, [item1, item2])

    def test_items_with_negative_price(self):
        item1 = {'name': 'Item 1', 'price': -5}
        item2 = {'name': 'Item 2', 'price': -4}
        item3 = {'name': 'Item 3', 'price': -3}
        items = [item1, item2, item3]
        result = cheap_items(items, 2)
        self.assertEqual(result, [item3, item2])
