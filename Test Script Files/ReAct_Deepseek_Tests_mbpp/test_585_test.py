import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):

    def test_typical_case(self):
        items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 200},
            {'name': 'item3', 'price': 300},
            {'name': 'item4', 'price': 400},
            {'name': 'item5', 'price': 500},
        ]
        n = 3
        result = expensive_items(items, n)
        self.assertEqual(len(result), n)
        self.assertEqual(result, [{'name': 'item5', 'price': 500},
                                   {'name': 'item4', 'price': 400},
                                   {'name': 'item3', 'price': 300}])

    def test_edge_case_n_greater_than_items(self):
        items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 200},
        ]
        n = 5
        result = expensive_items(items, n)
        self.assertEqual(len(result), len(items))
        self.assertEqual(result, [{'name': 'item2', 'price': 200},
                                   {'name': 'item1', 'price': 100}])

    def test_edge_case_n_equals_zero(self):
        items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 200},
            {'name': 'item3', 'price': 300},
        ]
        n = 0
        result = expensive_items(items, n)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])

    def test_edge_case_empty_items(self):
        items = []
        n = 3
        result = expensive_items(items, n)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])
