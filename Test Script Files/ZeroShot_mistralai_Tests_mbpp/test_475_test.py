import unittest
from mbpp_475_code import Counter

def sort_counter(dict1):
    x = Counter(dict1)
    sort_counter = x.most_common()
    return sort_counter

class TestSortCounter(unittest.TestCase):

    def test_empty_dict(self):
        self.assertListEqual(sort_counter({}), [])

    def test_single_item_dict(self):
        self.assertListEqual(sort_counter({'a': 1}), [('a', 1)])

    def test_multiple_items_dict(self):
        self.assertListEqual(sort_counter({'a': 3, 'b': 2, 'c': 1}), [('a', 3), ('b', 2), ('c', 1)])

    def test_duplicate_items_dict(self):
        self.assertListEqual(sort_counter({'a': 2, 'b': 2, 'c': 1}), [('a', 2), ('b', 2), ('c', 1)])
