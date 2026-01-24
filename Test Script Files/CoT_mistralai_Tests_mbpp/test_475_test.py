import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(sort_counter({}), [])

    def test_single_item_dict(self):
        self.assertEqual(sort_counter({'a': 1}), [('a', 1)])

    def test_multiple_items_dict(self):
        self.assertEqual(sort_counter({'a': 3, 'b': 2, 'c': 1}), [('a', 3), ('b', 2), ('c', 1)])

    def test_duplicate_items_dict(self):
        self.assertEqual(sort_counter({'a': 2, 'b': 2, 'c': 1}), [('a', 2), ('b', 2), ('c', 1)])

    def test_sort_counter_with_list(self):
        self.assertEqual(sort_counter([1, 2, 2, 3, 3, 3]), [('3', 3), ('2', 2), ('1', 1)])

    def test_sort_counter_with_string_keys(self):
        self.assertEqual(sort_counter({'apple': 3, 'banana': 2, 'orange': 1}), [('orange', 1), ('banana', 2), ('apple', 3)])

    def test_sort_counter_with_negative_values(self):
        self.assertEqual(sort_counter({'a': -1, 'b': 2, 'c': -3}), [('b', 2), ('a', -1), ('c', -3)])

    def test_sort_counter_with_floats(self):
        self.assertEqual(sort_counter({1.0: 3, 2.0: 2, 3.0: 1}), [('3.0', 1), ('2.0', 2), ('1.0', 3)])
