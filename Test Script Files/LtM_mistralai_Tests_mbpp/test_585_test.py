import unittest
from mbpp_585_code import expensive_items

class TestExpensiveItems(unittest.TestCase):

    def test_simple(self):
        items = [{'name': 'item1', 'price': 10}, {'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 30}]
        self.assertListEqual(expensive_items(items, 2), [{'name': 'item2', 'price': 20}, {'name': 'item3', 'price': 30}])

    def test_edge_cases(self):
        self.assertListEqual(expensive_items([], 1), [])
        self.assertListEqual(expensive_items([{'name': 'item1', 'price': 1}], 1), [{'name': 'item1', 'price': 1}])
        self.assertListEqual(expensive_items([{'name': 'item1', 'price': 1}], 2), [{'name': 'item1', 'price': 1}])

    def test_complex(self):
        items = [{'name': 'item1', 'price': 1}, {'name': 'item2', 'price': 2}, {'name': 'item3', 'price': 3},
                 {'name': 'item4', 'price': 4}, {'name': 'item5', 'price': 5}, {'name': 'item6', 'price': 6}]
        self.assertListEqual(expensive_items(items, 3), [{'name': 'item6', 'price': 6}, {'name': 'item5', 'price': 5},
                                                          {'name': 'item4', 'price': 4}])
        self.assertListEqual(expensive_items(items, 4), [{'name': 'item6', 'price': 6}, {'name': 'item5', 'price': 5},
                                                          {'name': 'item4', 'price': 4}, {'name': 'item3', 'price': 3}])
        self.assertListEqual(expensive_items(items, 5), [{'name': 'item6', 'price': 6}, {'name': 'item5', 'price': 5},
                                                          {'name': 'item4', 'price': 4}, {'name': 'item3', 'price': 3},
                                                          {'name': 'item2', 'price': 2}])
        self.assertListEqual(expensive_items(items, 6), [{'name': 'item6', 'price': 6}, {'name': 'item5', 'price': 5},
                                                          {'name': 'item4', 'price': 4}, {'name': 'item3', 'price': 3},
                                                          {'name': 'item2', 'price': 2}, {'name': 'item1', 'price': 1}])
