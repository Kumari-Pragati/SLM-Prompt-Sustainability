import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):
    def test_typical_use_case(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}, {'price': 3, 'name': 'D'}, {'price': 7, 'name': 'E'}]
        n = 3
        result = cheap_items(items, n)
        self.assertEqual(len(result), n)
        for item in result:
            self.assertIn(item, items)

    def test_edge_case_n_zero(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}, {'price': 3, 'name': 'D'}, {'price': 7, 'name': 'E'}]
        n = 0
        result = cheap_items(items, n)
        self.assertEqual(result, [])

    def test_edge_case_n_greater_than_items(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}, {'price': 3, 'name': 'D'}, {'price': 7, 'name': 'E'}]
        n = 10
        result = cheap_items(items, n)
        self.assertEqual(len(result), len(items))

    def test_invalid_input_non_integer_n(self):
        items = [{'price': 10, 'name': 'A'}, {'price': 5, 'name': 'B'}, {'price': 8, 'name': 'C'}, {'price': 3, 'name': 'D'}, {'price': 7, 'name': 'E'}]
        n = 'three'
        with self.assertRaises(TypeError):
            cheap_items(items, n)
