import unittest
from mbpp_795_code import cheap_items

class TestCheapItems(unittest.TestCase):

    def test_typical_case(self):
        items = [{'name': 'item1', 'price': 5},
                  {'name': 'item2', 'price': 10},
                  {'name': 'item3', 'price': 15},
                  {'name': 'item4', 'price': 20}]
        n = 2
        expected = [{'name': 'item1', 'price': 5},
                    {'name': 'item2', 'price': 10}]
        self.assertListEqual(cheap_items(items, n), expected)

    def test_edge_case_single_item(self):
        items = [{'name': 'item1', 'price': 5}]
        n = 1
        expected = [{'name': 'item1', 'price': 5}]
        self.assertListEqual(cheap_items(items, n), expected)

    def test_edge_case_no_items(self):
        items = []
        n = 1
        expected = []
        self.assertListEqual(cheap_items(items, n), expected)

    def test_edge_case_n_larger_than_len(self):
        items = [{'name': 'item1', 'price': 5}]
        n = len(items) + 1
        expected = []
        self.assertListEqual(cheap_items(items, n), expected)

    def test_corner_case_same_prices(self):
        items = [{'name': 'item1', 'price': 1},
                  {'name': 'item2', 'price': 1},
                  {'name': 'item3', 'price': 1}]
        n = 2
        expected = [{'name': 'item1', 'price': 1},
                    {'name': 'item2', 'price': 1}]
        self.assertListEqual(cheap_items(items, n), expected)
