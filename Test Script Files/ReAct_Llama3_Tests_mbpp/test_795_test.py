import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):
    def test_typical_case(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 7, 'name': 'C'}]
        n = 2
        result = cheap_items(items, n)
        self.assertEqual(len(result), n)
        self.assertEqual(result[0]['name'], 'B')
        self.assertEqual(result[1]['name'], 'C')

    def test_edge_case_n_zero(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 7, 'name': 'C'}]
        n = 0
        result = cheap_items(items, n)
        self.assertEqual(result, [])

    def test_edge_case_n_equal_to_items_length(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 7, 'name': 'C'}]
        n = len(items)
        result = cheap_items(items, n)
        self.assertEqual(result, items)

    def test_error_case_non_integer_n(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 7, 'name': 'C'}]
        n = 'a'
        with self.assertRaises(TypeError):
            cheap_items(items, n)

    def test_error_case_non_list_items(self):
        items = 'not a list'
        n = 2
        with self.assertRaises(TypeError):
            cheap_items(items, n)
