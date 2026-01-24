import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):

    def test_simple(self):
        items = [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 30}]
        self.assertListEqual(cheap_items(items, 2), [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}])

    def test_edge_cases(self):
        self.assertListEqual(cheap_items([], 1), [])
        self.assertListEqual(cheap_items([{'price': 1}], 1), [{'price': 1}])
        self.assertListEqual(cheap_items([{'price': 1}], 2), [{'price': 1}])

    def test_complex(self):
        items = [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 30},
                 {'name': 'item4', 'price': 1}, {'name': 'item5', 'price': 2000}]
        self.assertListEqual(cheap_items(items, 3), [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20},
                                                      {'name': 'item4', 'price': 1}])
