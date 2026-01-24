import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):
    def test_typical_use_case(self):
        items = [
            {'name': 'item1', 'price': 10},
            {'name': 'item2', 'price': 20},
            {'name': 'item3', 'price': 5},
            {'name': 'item4', 'price': 15},
        ]
        n = 2
        result = cheap_items(items, n)
        self.assertEqual(len(result), n)
        self.assertEqual(result[0]['price'], 5)
        self.assertEqual(result[1]['price'], 10)

    def test_edge_case_n_equals_zero(self):
        items = [
            {'name': 'item1', 'price': 10},
            {'name': 'item2', 'price': 20},
        ]
        n = 0
        result = cheap_items(items, n)
        self.assertEqual(len(result), 0)

    def test_boundary_case_n_equals_length_of_items(self):
        items = [
            {'name': 'item1', 'price': 10},
            {'name': 'item2', 'price': 20},
            {'name': 'item3', 'price': 5},
        ]
        n = len(items)
        result = cheap_items(items, n)
        self.assertEqual(len(result), n)
        self.assertEqual(result, items)

    def test_invalid_input_n_greater_than_length_of_items(self):
        items = [
            {'name': 'item1', 'price': 10},
            {'name': 'item2', 'price': 20},
            {'name': 'item3', 'price': 5},
        ]
        n = len(items) + 1
        with self.assertRaises(IndexError):
            cheap_items(items, n)
