import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):

    def setUp(self):
        self.items = [
            {'name': 'item1', 'price': 10},
            {'name': 'item2', 'price': 20},
            {'name': 'item3', 'price': 5},
            {'name': 'item4', 'price': 15},
            {'name': 'item5', 'price': 5},
        ]

    def test_n_greater_than_zero(self):
        self.assertEqual(cheap_items(self.items, 0), [])
        self.assertEqual(cheap_items(self.items, 1), [{'name': 'item5', 'price': 5}])
        self.assertEqual(cheap_items(self.items, 3), [{'name': 'item5', 'price': 5}, {'name': 'item3', 'price': 5}, {'name': 'item1', 'price': 10}])

    def test_n_equals_zero(self):
        self.assertEqual(cheap_items(self.items, 0), [])

    def test_n_equals_length_of_items(self):
        self.assertEqual(cheap_items(self.items, len(self.items)), self.items)

    def test_n_greater_than_length_of_items(self):
        self.assertEqual(cheap_items(self.items, len(self.items) + 1), self.items)

    def test_items_is_empty(self):
        self.assertEqual(cheap_items([], 3), [])

    def test_items_contains_negative_price(self):
        self.items.append({'name': 'item6', 'price': -10})
        self.assertEqual(cheap_items(self.items, 1), [{'name': 'item5', 'price': 5}])

    def test_items_contains_non_numeric_price(self):
        self.items.append({'name': 'item6', 'price': 'ten'})
        with self.assertRaises(TypeError):
            cheap_items(self.items, 1)
