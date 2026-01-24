import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            expensive_items([], 1)

    def test_single_item(self):
        item = {'name': 'Item 1', 'price': 100}
        result = expensive_items([item], 1)
        self.assertEqual(result, [item])

    def test_multiple_items_one_expensive(self):
        item1 = {'name': 'Item 1', 'price': 10}
        item2 = {'name': 'Item 2', 'price': 100}
        items = [item1, item2]
        result = expensive_items(items, 1)
        self.assertEqual(result, [item2])

    def test_multiple_items_multiple_expensive(self):
        item1 = {'name': 'Item 1', 'price': 10}
        item2 = {'name': 'Item 2', 'price': 50}
        item3 = {'name': 'Item 3', 'price': 100}
        items = [item1, item2, item3]
        result = expensive_items(items, 2)
        self.assertCountEqual(result, [item3, item2])

    def test_multiple_items_more_than_n(self):
        item1 = {'name': 'Item 1', 'price': 10}
        item2 = {'name': 'Item 2', 'price': 50}
        item3 = {'name': 'Item 3', 'price': 100}
        item4 = {'name': 'Item 4', 'price': 150}
        items = [item1, item2, item3, item4]
        result = expensive_items(items, 2)
        self.assertCountEqual(result, [item4, item3])

    def test_items_with_same_price(self):
        item1 = {'name': 'Item 1', 'price': 100}
        item2 = {'name': 'Item 2', 'price': 100}
        items = [item1, item2]
        result = expensive_items(items, 1)
        self.assertEqual(result, [item1])
