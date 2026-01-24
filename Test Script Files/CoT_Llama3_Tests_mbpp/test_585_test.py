import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):
    def test_typical_case(self):
        items = [{'name': 'A', 'price': 10}, {'name': 'B', 'price': 5}, {'name': 'C', 'price': 15}]
        n = 2
        self.assertEqual(expensive_items(items, n), [{'name': 'C', 'price': 15}, {'name': 'A', 'price': 10}])

    def test_edge_case_n_zero(self):
        items = [{'name': 'A', 'price': 10}, {'name': 'B', 'price': 5}, {'name': 'C', 'price': 15}]
        n = 0
        self.assertEqual(expensive_items(items, n), [])

    def test_edge_case_n_equal_to_length(self):
        items = [{'name': 'A', 'price': 10}, {'name': 'B', 'price': 5}, {'name': 'C', 'price': 15}]
        n = len(items)
        self.assertEqual(expensive_items(items, n), items)

    def test_invalid_input_non_integer_n(self):
        items = [{'name': 'A', 'price': 10}, {'name': 'B', 'price': 5}, {'name': 'C', 'price': 15}]
        n = 'a'
        with self.assertRaises(TypeError):
            expensive_items(items, n)

    def test_invalid_input_non_list_items(self):
        items = 'not a list'
        n = 2
        with self.assertRaises(TypeError):
            expensive_items(items, n)
