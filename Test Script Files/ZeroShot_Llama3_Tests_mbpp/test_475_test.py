import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):

    def test_sort_counter(self):
        self.assertEqual(sort_counter({'a': 3, 'b': 2, 'c': 1}), [('a', 3), ('b', 2), ('c', 1)])

    def test_sort_counter_empty(self):
        self.assertEqual(sort_counter({}), [])

    def test_sort_counter_single_element(self):
        self.assertEqual(sort_counter({'a': 1}), [('a', 1)])

    def test_sort_counter_multiple_elements(self):
        self.assertEqual(sort_counter({'a': 3, 'b': 2, 'c': 1, 'd': 4, 'e': 3}), [('d', 4), ('e', 3), ('a', 3), ('b', 2), ('c', 1)])
