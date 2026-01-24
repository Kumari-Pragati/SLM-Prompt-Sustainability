import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):

    def test_typical_case(self):
        items = [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 5}]
        n = 2
        expected_output = [{'name': 'item3', 'price': 5}, {'name': 'item1', 'price': 10}]
        self.assertEqual(cheap_items(items, n), expected_output)

    def test_edge_case_n_equals_zero(self):
        items = [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 5}]
        n = 0
        expected_output = []
        self.assertEqual(cheap_items(items, n), expected_output)

    def test_edge_case_n_greater_than_items(self):
        items = [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 5}]
        n = 5
        expected_output = [{'name': 'item3', 'price': 5}, {'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}]
        self.assertEqual(cheap_items(items, n), expected_output)

    def test_corner_case_duplicate_prices(self):
        items = [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 10}]
        n = 2
        expected_output = [{'name': 'item3', 'price': 10}, {'name': 'item1', 'price': 10}]
        self.assertEqual(cheap_items(items, n), expected_output)

    def test_invalid_input_n_negative(self):
        items = [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 5}]
        n = -1
        with self.assertRaises(Exception):
            cheap_items(items, n)
