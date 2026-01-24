import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):
    def test_sorted_list(self):
        self.assertEqual(sort_counter({'a': 3, 'b': 2, 'c': 1}), [('a', 3), ('b', 2), ('c', 1)])

    def test_empty_dict(self):
        self.assertEqual(sort_counter({}), [])

    def test_single_item_dict(self):
        self.assertEqual(sort_counter({'a': 1}), [('a', 1)])

    def test_negative_values(self):
        self.assertEqual(sort_counter({'a': -1, 'b': 2}), [('b', 2), ('a', -1)])
