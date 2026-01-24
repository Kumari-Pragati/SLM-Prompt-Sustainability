import unittest
from mbpp_475_code import Counter
from 475_code import sort_counter

class TestSortCounter(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(sort_counter({'a': 2, 'b': 1, 'c': 3}), [('c', 3), ('a', 2), ('b', 1)])

    def test_edge_cases(self):
        self.assertListEqual(sort_counter({'a': 0, 'b': 1}), [('b', 1)])
        self.assertListEqual(sort_counter({'a': 1, 'b': 2}), [('b', 2), ('a', 1)])
        self.assertListEqual(sort_counter({'a': 1, 'b': 1}), [('b', 1), ('a', 1)])

    def test_boundary_cases(self):
        self.assertListEqual(sort_counter({'a': float('inf'), 'b': float('inf')}), [('a', 1), ('b', 1)])
        self.assertListEqual(sort_counter({'a': -float('inf'), 'b': -float('inf')}), [('b', 1), ('a', 1)])

    def test_invalid_input(self):
        self.assertRaises(TypeError, sort_counter, 123)
