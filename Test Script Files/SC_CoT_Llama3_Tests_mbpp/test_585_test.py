import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):
    def test_typical_input(self):
        items = [{'price': 10, 'name': 'Item1'}, {'price': 5, 'name': 'Item2'}, {'price': 8, 'name': 'Item3'}, {'price': 15, 'name': 'Item4'}, {'price': 7, 'name': 'Item5'}]
        n = 3
        self.assertEqual(expensive_items(items, n), [{'price': 15, 'name': 'Item4'}, {'price': 10, 'name': 'Item1'}, {'price': 8, 'name': 'Item3'}])

    def test_edge_case_n_zero(self):
        items = [{'price': 10, 'name': 'Item1'}, {'price': 5, 'name': 'Item2'}, {'price': 8, 'name': 'Item3'}, {'price': 15, 'name': 'Item4'}, {'price': 7, 'name': 'Item5'}]
        n = 0
        self.assertEqual(expensive_items(items, n), [])

    def test_edge_case_n_equal_to_length(self):
        items = [{'price': 10, 'name': 'Item1'}, {'price': 5, 'name': 'Item2'}, {'price': 8, 'name': 'Item3'}, {'price': 15, 'name': 'Item4'}, {'price': 7, 'name': 'Item5'}]
        n = len(items)
        self.assertEqual(expensive_items(items, n), items)

    def test_edge_case_n_greater_than_length(self):
        items = [{'price': 10, 'name': 'Item1'}, {'price': 5, 'name': 'Item2'}, {'price': 8, 'name': 'Item3'}, {'price': 15, 'name': 'Item4'}, {'price': 7, 'name': 'Item5'}]
        n = len(items) + 1
        self.assertEqual(expensive_items(items, n), items)

    def test_invalid_input_non_integer_n(self):
        items = [{'price': 10, 'name': 'Item1'}, {'price': 5, 'name': 'Item2'}, {'price': 8, 'name': 'Item3'}, {'price': 15, 'name': 'Item4'}, {'price': 7, 'name': 'Item5'}]
        n = 'invalid'
        with self.assertRaises(TypeError):
            expensive_items(items, n)

    def test_invalid_input_non_list_items(self):
        items = 'invalid'
        n = 3
        with self.assertRaises(TypeError):
            expensive_items(items, n)
