import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sort_counter({'a': 2, 'b': 1}), [('a', 2), ('b', 1)])

    def test_empty_input(self):
        self.assertEqual(sort_counter({}), [])

    def test_single_element_input(self):
        self.assertEqual(sort_counter({'a': 1}), [('a', 1)])

    def test_multiple_same_frequency(self):
        self.assertEqual(sort_counter({'a': 2, 'b': 2}), [('a', 2), ('b', 2)])

    def test_negative_values(self):
        self.assertEqual(sort_counter({'a': -2, 'b': -1}), [('a', -2), ('b', -1)])

    def test_mixed_values(self):
        self.assertEqual(sort_counter({'a': 2, 'b': -1, 'c': 0}), [('a', 2), ('b', -1), ('c', 0)])

    def test_large_input(self):
        self.assertEqual(sort_counter({'a': 1000, 'b': 999, 'c': 998}), [('a', 1000), ('b', 999), ('c', 998)])
