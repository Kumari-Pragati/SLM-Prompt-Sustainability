import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual(sort_counter({}), [])

    def test_single_key(self):
        self.assertEqual(sort_counter({'a': 1}), [('a', 1)])

    def test_multiple_keys(self):
        self.assertEqual(sort_counter({'a': 3, 'b': 2, 'c': 1}), [('a', 3), ('b', 2), ('c', 1)])

    def test_keys_with_same_value(self):
        self.assertEqual(sort_counter({'a': 2, 'b': 2, 'c': 1}), [('a', 2), ('b', 2), ('c', 1)])

    def test_keys_with_negative_values(self):
        self.assertEqual(sort_counter({'a': 2, 'b': -2, 'c': 1}), [('a', 2), ('b', -2), ('c', 1)])

    def test_keys_with_zero_values(self):
        self.assertEqual(sort_counter({'a': 0, 'b': 0, 'c': 1}), [('c', 1), ('a', 0), ('b', 0)])

    def test_keys_with_non_integer_values(self):
        self.assertEqual(sort_counter({'a': 2.5, 'b': -2.5, 'c': 1}), [('c', 1), ('a', 2.5), ('b', -2.5)])

    def test_keys_with_non_dict_input(self):
        with self.assertRaises(TypeError):
            sort_counter('not a dict')
