import unittest
from mbpp_585_code import namedtuple
from heapq import nlargest

Item = namedtuple('Item', ['name', 'price'])

def expensive_items(items, n):
    return nlargest(n, items, key=lambda s: s.price)

class TestExpensiveItems(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(expensive_items([], 1), [])

    def test_single_item(self):
        item = Item('Item1', 100)
        self.assertListEqual(expensive_items([item], 1), [item])

    def test_multiple_items(self):
        item1 = Item('Item1', 200)
        item2 = Item('Item2', 150)
        item3 = Item('Item3', 100)
        items = [item1, item2, item3]
        self.assertListEqual(expensive_items(items, 2), [item1, item2])

    def test_multiple_items_with_duplicates(self):
        item1 = Item('Item1', 200)
        item2 = Item('Item2', 150)
        item3 = Item('Item3', 100)
        item4 = Item('Item1', 200)
        items = [item1, item2, item3, item4]
        self.assertListEqual(expensive_items(items, 2), [item1, item4])
