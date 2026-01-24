import unittest
from mbpp_795_code import namedtuple
from heapq import nsmallest

Item = namedtuple('Item', ['name', 'price'])

class TestCheapItems(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(cheap_items([], 1), [])

    def test_single_item(self):
        item = Item('Item1', 10)
        self.assertListEqual(cheap_items([item], 1), [item])

    def test_multiple_items(self):
        items = [
            Item('Item1', 5),
            Item('Item2', 10),
            Item('Item3', 15),
            Item('Item4', 20)
        ]
        expected = [items[0], items[1]]
        self.assertListEqual(cheap_items(items, 2), expected)

    def test_n_larger_than_len(self):
        items = [
            Item('Item1', 5),
            Item('Item2', 10),
            Item('Item3', 15),
            Item('Item4', 20)
        ]
        self.assertListEqual(cheap_items(items, len(items) + 1), items)
