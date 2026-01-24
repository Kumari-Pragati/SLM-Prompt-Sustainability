import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):
    def test_typical_case(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}, {'price': 12, 'name': 'D'}, {'price': 7, 'name': 'E'}]
        n = 3
        result = expensive_items(items, n)
        self.assertEqual(result, [{'price': 12, 'name': 'D'}, {'price': 10, 'name': 'A'}, {'price': 8, 'name': 'C'}])

    def test_edge_case_n_zero(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}, {'price': 12, 'name': 'D'}, {'price': 7, 'name': 'E'}]
        n = 0
        result = expensive_items(items, n)
        self.assertEqual(result, [])

    def test_edge_case_n_equal_to_length(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}, {'price': 12, 'name': 'D'}, {'price': 7, 'name': 'E'}]
        n = len(items)
        result = expensive_items(items, n)
        self.assertEqual(result, items)

    def test_error_case_invalid_n_type(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}, {'price': 12, 'name': 'D'}, {'price': 7, 'name': 'E'}]
        n = 'invalid'
        with self.assertRaises(TypeError):
            expensive_items(items, n)
