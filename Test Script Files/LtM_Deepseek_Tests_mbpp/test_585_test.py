import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):

    def test_simple_input(self):
        items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 200},
            {'name': 'item3', 'price': 300}
        ]
        n = 2
        result = expensive_items(items, n)
        self.assertEqual(result, [{'name': 'item3', 'price': 300}, {'name': 'item2', 'price': 200}])

    def test_edge_case_empty_input(self):
        items = []
        n = 2
        result = expensive_items(items, n)
        self.assertEqual(result, [])

    def test_edge_case_n_greater_than_items(self):
        items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 200},
            {'name': 'item3', 'price': 300}
        ]
        n = 5
        result = expensive_items(items, n)
        self.assertEqual(result, items)

    def test_boundary_case_n_equals_1(self):
        items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 200},
            {'name': 'item3', 'price': 300}
        ]
        n = 1
        result = expensive_items(items, n)
        self.assertEqual(result, [{'name': 'item3', 'price': 300}])

    def test_complex_case_duplicate_prices(self):
        items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 200},
            {'name': 'item3', 'price': 300},
            {'name': 'item4', 'price': 300}
        ]
        n = 3
        result = expensive_items(items, n)
        self.assertEqual(result, [{'name': 'item3', 'price': 300}, {'name': 'item4', 'price': 300}, {'name': 'item2', 'price': 200}])
