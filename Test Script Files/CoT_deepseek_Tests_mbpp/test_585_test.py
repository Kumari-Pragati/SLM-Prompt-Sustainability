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
        self.assertEqual(result, [{'name': 'item5', 'price': 500}, {'name': 'item4', 'price': 400}, {'name': 'item3', 'price': 300}])

    def test_edge_case_n_greater_than_items(self):
        items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 200},
        ]
        n = 5
        result = expensive_items(items, n)
        self.assertEqual(result, [{'name': 'item2', 'price': 200}, {'name': 'item1', 'price': 100}])

    def test_edge_case_n_equal_to_items(self):
        items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 200},
            {'name': 'item3', 'price': 300},
        ]
        n = 3
        result = expensive_items(items, n)
        self.assertEqual(result, [{'name': 'item3', 'price': 300}, {'name': 'item2', 'price': 200}, {'name': 'item1', 'price': 100}])

    def test_edge_case_n_equal_to_zero(self):
        items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 200},
            {'name': 'item3', 'price': 300},
        ]
        n = 0
        result = expensive_items(items, n)
        self.assertEqual(result, [])

    def test_edge_case_n_less_than_zero(self):
        items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 200},
            {'name': 'item3', 'price': 300},
        ]
        n = -1
        with self.assertRaises(ValueError):
            expensive_items(items, n)

    def test_invalid_input_type(self):
        items = "not a list"
        n = 3
        with self.assertRaises(TypeError):
            expensive_items(items, n)
