import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):
    def test_simple(self):
        items = [{'price': 1, 'name': 'item1'}, {'price': 2, 'name': 'item2'}, {'price': 3, 'name': 'item3'}]
        n = 2
        result = cheap_items(items, n)
        self.assertEqual(result, [{'price': 1, 'name': 'item1'}, {'price': 2, 'name': 'item2'}])

    def test_empty_input(self):
        items = []
        n = 2
        with self.assertRaises(IndexError):
            cheap_items(items, n)

    def test_invalid_input(self):
        items = [{'price': 1, 'name': 'item1'}, {'price': 2, 'name': 'item2'}, {'price': 3, 'name': 'item3'}]
        n = -1
        with self.assertRaises(ValueError):
            cheap_items(items, n)

    def test_max_input(self):
        items = [{'price': 1, 'name': 'item1'}, {'price': 2, 'name': 'item2'}, {'price': 3, 'name': 'item3'}]
        n = len(items)
        result = cheap_items(items, n)
        self.assertEqual(result, items)

    def test_max_input_edge(self):
        items = [{'price': 1, 'name': 'item1'}, {'price': 2, 'name': 'item2'}]
        n = len(items)
        result = cheap_items(items, n)
        self.assertEqual(result, items)

    def test_max_input_edge2(self):
        items = [{'price': 1, 'name': 'item1'}]
        n = len(items)
        result = cheap_items(items, n)
        self.assertEqual(result, items)
