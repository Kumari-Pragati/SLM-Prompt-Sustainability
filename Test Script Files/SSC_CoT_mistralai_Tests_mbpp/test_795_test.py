import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):
    def test_normal_operation(self):
        items = [{'name': 'item1', 'price': 5},
                  {'name': 'item2', 'price': 10},
                  {'name': 'item3', 'price': 3},
                  {'name': 'item4', 'price': 15}]
        result = cheap_items(items, 2)
        expected = [{'name': 'item3', 'price': 3}, {'name': 'item1', 'price': 5}]
        self.assertListEqual(result, expected)

    def test_edge_cases(self):
        items = [{'name': 'item1', 'price': 5},
                  {'name': 'item2', 'price': 10},
                  {'name': 'item3', 'price': 3},
                  {'name': 'item4', 'price': 1}]
        result = cheap_items(items, 4)
        expected = [{'name': 'item1', 'price': 5},
                    {'name': 'item3', 'price': 3},
                    {'name': 'item4', 'price': 1},
                    {'name': 'item2', 'price': 10}]
        self.assertListEqual(result, expected)

        items = [{'name': 'item1', 'price': 5}]
        result = cheap_items(items, 2)
        expected = [{'name': 'item1', 'price': 5}]
        self.assertListEqual(result, expected)

        items = []
        result = cheap_items(items, 2)
        expected = []
        self.assertListEqual(result, expected)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            cheap_items(1, 2)

        with self.assertRaises(TypeError):
            cheap_items('string', 2)
