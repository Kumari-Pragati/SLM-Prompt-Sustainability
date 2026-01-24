import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):

    def test_typical_case(self):
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

    def test_edge_case_n_greater_than_items(self):
        items = [
            {'name': 'item1', 'price': 10},
            {'name': 'item2', 'price': 20},
        ]
        n = 3
        result = cheap_items(items, n)
        self.assertEqual(len(result), len(items))

    def test_edge_case_n_zero(self):
        items = [
            {'name': 'item1', 'price': 10},
            {'name': 'item2', 'price': 20},
        ]
        n = 0
        result = cheap_items(items, n)
        self.assertEqual(len(result), 0)

    def test_edge_case_empty_items(self):
        items = []
        n = 2
        result = cheap_items(items, n)
        self.assertEqual(len(result), 0)

    def test_error_case_non_list_items(self):
        items = {}
        n = 2
        with self.assertRaises(TypeError):
            cheap_items(items, n)

    def test_error_case_non_integer_n(self):
        items = [
            {'name': 'item1', 'price': 10},
            {'name': 'item2', 'price': 20},
        ]
        n = 'two'
        with self.assertRaises(TypeError):
            cheap_items(items, n)
