import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):
    def test_typical_case(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}]
        n = 2
        self.assertEqual(cheap_items(items, n), [{'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}])

    def test_edge_case_n_zero(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}]
        n = 0
        self.assertEqual(cheap_items(items, n), [])

    def test_edge_case_n_equal_to_length(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}]
        n = 3
        self.assertEqual(cheap_items(items, n), items)

    def test_edge_case_n_greater_than_length(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}]
        n = 4
        self.assertEqual(cheap_items(items, n), items)

    def test_invalid_input_type(self):
        items = 'Invalid input'
        n = 2
        with self.assertRaises(TypeError):
            cheap_items(items, n)

    def test_invalid_input_type2(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}]
        n = 'Invalid input'
        with self.assertRaises(TypeError):
            cheap_items(items, n)
