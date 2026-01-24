import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):
    def test_typical_case(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}]
        n = 2
        self.assertEqual(expensive_items(items, n), [{'price': 10, 'name': 'A'}, {'price': 8, 'name': 'C'}])

    def test_edge_case_n_zero(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}]
        n = 0
        self.assertEqual(expensive_items(items, n), [])

    def test_edge_case_n_equal_to_length(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}]
        n = len(items)
        self.assertEqual(expensive_items(items, n), items)

    def test_edge_case_n_greater_than_length(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}]
        n = len(items) + 1
        self.assertEqual(expensive_items(items, n), items)

    def test_invalid_input_non_integer_n(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}]
        n = 'invalid'
        with self.assertRaises(TypeError):
            expensive_items(items, n)

    def test_invalid_input_non_list_items(self):
        items = 'invalid'
        n = 2
        with self.assertRaises(TypeError):
            expensive_items(items, n)
