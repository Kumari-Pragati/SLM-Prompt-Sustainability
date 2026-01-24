import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):
    def test_typical_input(self):
        items = [{'price': 10, 'name': 'Item1'}, {'price': 20, 'name': 'Item2'}, {'price': 5, 'name': 'Item3'}, {'price': 15, 'name': 'Item4'}, {'price': 25, 'name': 'Item5'}]
        n = 3
        self.assertEqual(cheap_items(items, n), [{'price': 5, 'name': 'Item3'}, {'price': 10, 'name': 'Item1'}, {'price': 15, 'name': 'Item4'}])

    def test_edge_case_n_zero(self):
        items = [{'price': 10, 'name': 'Item1'}, {'price': 20, 'name': 'Item2'}, {'price': 5, 'name': 'Item3'}, {'price': 15, 'name': 'Item4'}, {'price': 25, 'name': 'Item5'}]
        n = 0
        self.assertEqual(cheap_items(items, n), [])

    def test_edge_case_n_greater_than_items(self):
        items = [{'price': 10, 'name': 'Item1'}, {'price': 20, 'name': 'Item2'}, {'price': 5, 'name': 'Item3'}, {'price': 15, 'name': 'Item4'}, {'price': 25, 'name': 'Item5'}]
        n = 10
        self.assertEqual(cheap_items(items, n), items)

    def test_invalid_input_non_integer_n(self):
        items = [{'price': 10, 'name': 'Item1'}, {'price': 20, 'name': 'Item2'}, {'price': 5, 'name': 'Item3'}, {'price': 15, 'name': 'Item4'}, {'price': 25, 'name': 'Item5'}]
        n = 'five'
        with self.assertRaises(TypeError):
            cheap_items(items, n)

    def test_invalid_input_non_list_items(self):
        items = 123
        n = 3
        with self.assertRaises(TypeError):
            cheap_items(items, n)
