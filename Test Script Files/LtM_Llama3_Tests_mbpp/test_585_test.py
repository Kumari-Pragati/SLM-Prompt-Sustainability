import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):
    def test_simple(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}]
        n = 2
        result = expensive_items(items, n)
        self.assertEqual(result, [{'price': 10, 'name': 'A'}, {'price': 8, 'name': 'C'}])

    def test_empty_input(self):
        items = []
        n = 2
        with self.assertRaises(IndexError):
            expensive_items(items, n)

    def test_invalid_input(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}]
        n = 'a'
        with self.assertRaises(TypeError):
            expensive_items(items, n)

    def test_max_items(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}, {'price': 12, 'name': 'D'}]
        n = 4
        result = expensive_items(items, n)
        self.assertEqual(result, items)

    def test_min_items(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}]
        n = 1
        result = expensive_items(items, n)
        self.assertEqual(result, [{'price': 10, 'name': 'A'}])
