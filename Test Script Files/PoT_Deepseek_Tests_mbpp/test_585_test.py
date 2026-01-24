import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):

    def test_typical_case(self):
        items = [{'name': 'item1', 'price': 100}, {'name': 'item2', 'price': 200}, {'name': 'item3', 'price': 150}]
        n = 2
        expected_output = [{'name': 'item2', 'price': 200}, {'name': 'item3', 'price': 150}]
        self.assertEqual(expensive_items(items, n), expected_output)

    def test_edge_case_n_equals_zero(self):
        items = [{'name': 'item1', 'price': 100}, {'name': 'item2', 'price': 200}, {'name': 'item3', 'price': 150}]
        n = 0
        expected_output = []
        self.assertEqual(expensive_items(items, n), expected_output)

    def test_edge_case_n_equals_one(self):
        items = [{'name': 'item1', 'price': 100}, {'name': 'item2', 'price': 200}, {'name': 'item3', 'price': 150}]
        n = 1
        expected_output = [{'name': 'item2', 'price': 200}]
        self.assertEqual(expensive_items(items, n), expected_output)

    def test_edge_case_n_greater_than_items_length(self):
        items = [{'name': 'item1', 'price': 100}, {'name': 'item2', 'price': 200}, {'name': 'item3', 'price': 150}]
        n = 5
        expected_output = [{'name': 'item2', 'price': 200}, {'name': 'item3', 'price': 150}, {'name': 'item1', 'price': 100}]
        self.assertEqual(expensive_items(items, n), expected_output)

    def test_corner_case_empty_items(self):
        items = []
        n = 2
        expected_output = []
        self.assertEqual(expensive_items(items, n), expected_output)

    def test_corner_case_same_prices(self):
        items = [{'name': 'item1', 'price': 100}, {'name': 'item2', 'price': 100}, {'name': 'item3', 'price': 100}]
        n = 2
        expected_output = [{'name': 'item3', 'price': 100}, {'name': 'item2', 'price': 100}]
        self.assertEqual(expensive_items(items, n), expected_output)
