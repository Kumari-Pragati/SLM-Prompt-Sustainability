import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):

    def test_typical_case(self):
        items = [
            {'name': 'item1', 'price': 10},
            {'name': 'item2', 'price': 20},
            {'name': 'item3', 'price': 30},
            {'name': 'item4', 'price': 40},
            {'name': 'item5', 'price': 50}
        ]
        expected = [
            {'name': 'item5', 'price': 50},
            {'name': 'item4', 'price': 40},
            {'name': 'item3', 'price': 30}
        ]
        self.assertEqual(expensive_items(items, 3), expected)

    def test_edge_case_single_item(self):
        items = [{'name': 'item1', 'price': 100}]
        expected = [{'name': 'item1', 'price': 100}]
        self.assertEqual(expensive_items(items, 1), expected)

    def test_edge_case_no_items(self):
        items = []
        expected = []
        self.assertEqual(expensive_items(items, 1), expected)

    def test_edge_case_more_than_items(self):
        items = [
            {'name': 'item1', 'price': 10},
            {'name': 'item2', 'price': 20},
            {'name': 'item3', 'price': 30},
            {'name': 'item4', 'price': 40},
            {'name': 'item5', 'price': 50}
        ]
        expected = [
            {'name': 'item5', 'price': 50},
            {'name': 'item4', 'price': 40},
            {'name': 'item3', 'price': 30},
            {'name': 'item2', 'price': 20},
            {'name': 'item1', 'price': 10}
        ]
        self.assertEqual(expensive_items(items, 5), expected)
