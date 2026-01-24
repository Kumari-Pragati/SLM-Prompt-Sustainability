import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):
    def test_typical_input(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 7, 'name': 'C'}, {'price': 3, 'name': 'D'}, {'price': 9, 'name': 'E'}]
        n = 3
        result = cheap_items(items, n)
        self.assertEqual(result, [{'price': 3, 'name': 'D'}, {'price': 5, 'name': 'B'}, {'price': 7, 'name': 'C'}])

    def test_edge_case_n_zero(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 7, 'name': 'C'}, {'price': 3, 'name': 'D'}, {'price': 9, 'name': 'E'}]
        n = 0
        result = cheap_items(items, n)
        self.assertEqual(result, [])

    def test_edge_case_n_equal_to_length(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 7, 'name': 'C'}, {'price': 3, 'name': 'D'}, {'price': 9, 'name': 'E'}]
        n = 5
        result = cheap_items(items, n)
        self.assertEqual(result, items)

    def test_invalid_input_non_integer_n(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 7, 'name': 'C'}, {'price': 3, 'name': 'D'}, {'price': 9, 'name': 'E'}]
        n = 'a'
        with self.assertRaises(TypeError):
            cheap_items(items, n)

    def test_invalid_input_non_list_items(self):
        items = 'not a list'
        n = 3
        with self.assertRaises(TypeError):
            cheap_items(items, n)
