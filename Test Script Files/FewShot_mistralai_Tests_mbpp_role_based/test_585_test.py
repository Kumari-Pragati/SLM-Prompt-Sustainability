import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):
    def test_typical_use_case(self):
        items = [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 30}]
        result = expensive_items(items, 2)
        self.assertEqual(result, [{'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 30}])

    def test_empty_list(self):
        result = expensive_items([], 1)
        self.assertListEqual(result, [])

    def test_single_item(self):
        result = expensive_items([{'name': 'item1', 'price': 10}], 1)
        self.assertEqual(result, [{'name': 'item1', 'price': 10}])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            expensive_items('invalid', 1)
