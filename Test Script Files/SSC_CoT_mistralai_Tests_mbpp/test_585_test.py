import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):

    def test_typical_input(self):
        items = [
            {'name': 'Item1', 'price': 10},
            {'name': 'Item2', 'price': 20},
            {'name': 'Item3', 'price': 30},
            {'name': 'Item4', 'price': 40},
            {'name': 'Item5', 'price': 50}
        ]
        result = expensive_items(items, 3)
        expected = [
            {'name': 'Item5', 'price': 50},
            {'name': 'Item4', 'price': 40},
            {'name': 'Item3', 'price': 30}
        ]
        self.assertListEqual(result, expected)

    def test_edge_case_one_item(self):
        items = [{'name': 'Item1', 'price': 10}]
        result = expensive_items(items, 1)
        expected = [{'name': 'Item1', 'price': 10}]
        self.assertListEqual(result, expected)

    def test_edge_case_no_items(self):
        items = []
        result = expensive_items(items, 1)
        expected = []
        self.assertListEqual(result, expected)

    def test_edge_case_more_than_items(self):
        items = [
            {'name': 'Item1', 'price': 10},
            {'name': 'Item2', 'price': 20},
            {'name': 'Item3', 'price': 30},
            {'name': 'Item4', 'price': 40},
            {'name': 'Item5', 'price': 50}
        ]
        result = expensive_items(items, len(items) + 1)
        expected = items
        self.assertListEqual(result, expected)

    def test_edge_case_negative_n(self):
        with self.assertRaises(ValueError):
            expensive_items(items, -1)
