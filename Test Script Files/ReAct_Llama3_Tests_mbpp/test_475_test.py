import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual(sort_counter({}), [])

    def test_single_key(self):
        self.assertEqual(sort_counter({'a': 1}), [('a', 1)])

    def test_multiple_keys(self):
        self.assertEqual(sort_counter({'a': 2, 'b': 1, 'c': 3}), [('c', 3), ('a', 2), ('b', 1)])

    def test_keys_with_same_value(self):
        self.assertEqual(sort_counter({'a': 2, 'b': 2, 'c': 2}), [('a', 2), ('b', 2), ('c', 2)])

    def test_keys_with_negative_value(self):
        self.assertEqual(sort_counter({'a': -2, 'b': -1, 'c': 3}), [('c', 3), ('a', -2), ('b', -1)])

    def test_keys_with_zero_value(self):
        self.assertEqual(sort_counter({'a': 0, 'b': 0, 'c': 0}), [('a', 0), ('b', 0), ('c', 0)])

    def test_dict_with_non_integer_values(self):
        self.assertEqual(sort_counter({'a': 2.5, 'b': 1.0, 'c': 3.0}), [('c', 3.0), ('a', 2.5), ('b', 1.0)])

    def test_dict_with_non_string_keys(self):
        self.assertEqual(sort_counter({1: 2, 2: 1, 3: 3}), [(3, 3), (2, 1), (1, 2)])
