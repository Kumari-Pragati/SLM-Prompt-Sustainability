import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):

    def test_empty_dict(self):
        result = sort_counter({})
        self.assertEqual(result, [])

    def test_single_item_dict(self):
        result = sort_counter({'a': 1})
        self.assertEqual(result, [('a', 1)])

    def test_multiple_items_dict(self):
        result = sort_counter({'a': 2, 'b': 3, 'c': 1})
        self.assertEqual(result, [('c', 1), ('a', 2), ('b', 3)])

    def test_duplicate_items_dict(self):
        result = sort_counter({'a': 2, 'b': 2, 'c': 1})
        self.assertEqual(result, [('c', 1), ('a', 2), ('b', 2)])

    def test_negative_values_dict(self):
        result = sort_counter({'a': -2, 'b': 3, 'c': -1})
        self.assertEqual(result, [('c', -1), ('a', -2), ('b', 3)])

    def test_key_error_raises_ValueError(self):
        with self.assertRaises(ValueError):
            sort_counter({'a': 1, 'b': 1, 'c': 1}['d'])
