import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):
    def test_typical_use_case(self):
        items = [{'name': 'item1', 'price': 100}, 
                 {'name': 'item2', 'price': 50}, 
                 {'name': 'item3', 'price': 200}, 
                 {'name': 'item4', 'price': 30}]
        n = 2
        result = expensive_items(items, n)
        self.assertEqual(len(result), n)
        self.assertEqual(result[0]['name'], 'item3')
        self.assertEqual(result[1]['name'], 'item1')

    def test_edge_case_n_zero(self):
        items = [{'name': 'item1', 'price': 100}, 
                 {'name': 'item2', 'price': 50}, 
                 {'name': 'item3', 'price': 200}, 
                 {'name': 'item4', 'price': 30}]
        n = 0
        result = expensive_items(items, n)
        self.assertEqual(result, [])

    def test_edge_case_n_greater_than_items(self):
        items = [{'name': 'item1', 'price': 100}, 
                 {'name': 'item2', 'price': 50}, 
                 {'name': 'item3', 'price': 200}, 
                 {'name': 'item4', 'price': 30}]
        n = 5
        result = expensive_items(items, n)
        self.assertEqual(len(result), len(items))

    def test_invalid_input_non_integer_n(self):
        items = [{'name': 'item1', 'price': 100}, 
                 {'name': 'item2', 'price': 50}, 
                 {'name': 'item3', 'price': 200}, 
                 {'name': 'item4', 'price': 30}]
        n = 'invalid'
        with self.assertRaises(TypeError):
            expensive_items(items, n)
