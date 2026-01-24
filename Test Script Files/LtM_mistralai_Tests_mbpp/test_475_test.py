import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(sort_counter({'a': 2, 'b': 1, 'c': 3}), [('c', 3), ('a', 2), ('b', 1)])

    def test_single_value(self):
        self.assertListEqual(sort_counter({'a': 5}), [('a', 5)])

    def test_empty_input(self):
        self.assertListEqual(sort_counter({}), [])

    def test_reversed_order(self):
        self.assertListEqual(sort_counter({'a': 2, 'b': 1, 'c': 3}), [('b', 1), ('a', 2), ('c', 3)])

    def test_negative_values(self):
        self.assertListEqual(sort_counter({'a': -2, 'b': -1, 'c': -3}), [('c', -3), ('a', -2), ('b', -1)])
