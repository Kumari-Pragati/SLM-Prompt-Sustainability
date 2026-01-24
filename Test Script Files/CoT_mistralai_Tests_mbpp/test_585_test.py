import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(expensive_items([], 1), [])

    def test_single_item(self):
        item = {'name': 'Item1', 'price': 10}
        self.assertListEqual(expensive_items([item], 1), [item])

    def test_multiple_items_single_expensive(self):
        item1 = {'name': 'Item1', 'price': 1}
        item2 = {'name': 'Item2', 'price': 2}
        item3 = {'name': 'Item3', 'price': 3}
        self.assertListEqual(expensive_items([item1, item2, item3], 1), [item3])

    def test_multiple_items_multiple_expensive(self):
        item1 = {'name': 'Item1', 'price': 1}
        item2 = {'name': 'Item2', 'price': 2}
        item3 = {'name': 'Item3', 'price': 3}
        item4 = {'name': 'Item4', 'price': 4}
        self.assertListEqual(expensive_items([item1, item2, item3, item4], 2), [item4, item3])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            expensive_items('invalid', 1)

    def test_invalid_input_n(self):
        with self.assertRaises(ValueError):
            expensive_items([{'name': 'Item', 'price': 1}], -1)

    def test_invalid_input_items(self):
        with self.assertRaises(TypeError):
            expensive_items([1, 2, 3], [{'name': 'Item', 'price': 1}])
