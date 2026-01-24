import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):

    def setUp(self):
        self.items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 200},
            {'name': 'item3', 'price': 300},
            {'name': 'item4', 'price': 400},
            {'name': 'item5', 'price': 500},
        ]

    def test_n_greater_than_zero(self):
        self.assertEqual(len(expensive_items(self.items, 3)), 3)

    def test_n_equal_to_zero(self):
        self.assertEqual(expensive_items(self.items, 0), [])

    def test_n_greater_than_items_length(self):
        self.assertEqual(len(expensive_items(self.items, 10)), len(self.items))

    def test_items_with_same_price(self):
        items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 100},
            {'name': 'item3', 'price': 100},
        ]
        self.assertEqual(len(expensive_items(items, 2)), 2)

    def test_negative_n(self):
        with self.assertRaises(Exception):
            expensive_items(self.items, -1)

    def test_n_is_not_integer(self):
        with self.assertRaises(Exception):
            expensive_items(self.items, 'a')
