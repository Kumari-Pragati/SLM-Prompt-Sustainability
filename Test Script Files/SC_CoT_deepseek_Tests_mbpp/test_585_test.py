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
        expected_output = [
            {'name': 'item5', 'price': 500},
            {'name': 'item4', 'price': 400},
            {'name': 'item3', 'price': 300},
        ]
        self.assertEqual(expensive_items(items, n), expected_output)

    def test_edge_case_n_equals_zero(self):
        items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 200},
            {'name': 'item3', 'price': 300},
            {'name': 'item4', 'price': 400},
            {'name': 'item5', 'price': 500},
        ]
        n = 0
        expected_output = []
        self.assertEqual(expensive_items(items, n), expected_output)

    def test_edge_case_n_greater_than_length_of_items(self):
        items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 200},
            {'name': 'item3', 'price': 300},
            {'name': 'item4', 'price': 400},
            {'name': 'item5', 'price': 500},
        ]
        n = 10
        expected_output = items
        self.assertEqual(expensive_items(items, n), expected_output)

    def test_corner_case_empty_items(self):
        items = []
        n = 3
        expected_output = []
        self.assertEqual(expensive_items(items, n), expected_output)

    def test_invalid_input_n_is_negative(self):
        items = [
            {'name': 'item1', 'price': 100},
            {'name': 'item2', 'price': 200},
            {'name': 'item3', 'price': 300},
            {'name': 'item4', 'price': 400},
            {'name': 'item5', 'price': 500},
        ]
        n = -3
        with self.assertRaises(ValueError):
            expensive_items(items, n)
