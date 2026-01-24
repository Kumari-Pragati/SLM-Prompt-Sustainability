import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):

    def test_expensive_items(self):
        items = [{'name': 'item1', 'price': 100}, 
                 {'name': 'item2', 'price': 200}, 
                 {'name': 'item3', 'price': 50}, 
                 {'name': 'item4', 'price': 150}, 
                 {'name': 'item5', 'price': 250}]
        n = 3
        expected_result = [{'name': 'item5', 'price': 250}, 
                            {'name': 'item2', 'price': 200}, 
                            {'name': 'item4', 'price': 150}]
        self.assertEqual(expensive_items(items, n), expected_result)

    def test_expensive_items_empty_list(self):
        items = []
        n = 3
        self.assertEqual(expensive_items(items, n), [])

    def test_expensive_items_n_greater_than_length(self):
        items = [{'name': 'item1', 'price': 100}, 
                 {'name': 'item2', 'price': 200}, 
                 {'name': 'item3', 'price': 50}]
        n = 5
        self.assertEqual(expensive_items(items, n), items)

    def test_expensive_items_n_equal_to_length(self):
        items = [{'name': 'item1', 'price': 100}, 
                 {'name': 'item2', 'price': 200}, 
                 {'name': 'item3', 'price': 50}]
        n = 3
        self.assertEqual(expensive_items(items, n), items[:n])
