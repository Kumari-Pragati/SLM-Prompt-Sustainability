import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):

    def test_typical_case(self):
        items = [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 15}]
        n = 2
        expected_output = [{'name': 'item1', 'price': 10}, {'name': 'item3', 'price': 15}]
        self.assertEqual(cheap_items(items, n), expected_output)

    def test_edge_case_n_equals_0(self):
        items = [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 15}]
        n = 0
        expected_output = []
        self.assertEqual(cheap_items(items, n), expected_output)

    def test_edge_case_n_equals_len_items(self):
        items = [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 15}]
        n = len(items)
        expected_output = items
        self.assertEqual(cheap_items(items, n), expected_output)

    def test_corner_case_n_greater_than_len_items(self):
        items = [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 15}]
        n = len(items) + 1
        expected_output = items
        self.assertEqual(cheap_items(items, n), expected_output)

    def test_invalid_input_n_negative(self):
        items = [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 15}]
        n = -1
        with self.assertRaises(ValueError):
            cheap_items(items, n)

    def test_invalid_input_items_not_list(self):
        items = 'not a list'
        n = 2
        with self.assertRaises(TypeError):
            cheap_items(items, n)
