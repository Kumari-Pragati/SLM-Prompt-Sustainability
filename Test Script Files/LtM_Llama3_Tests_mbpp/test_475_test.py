import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(sort_counter({}), [])

    def test_single_element_input(self):
        self.assertEqual(sort_counter({'a': 1}), [('a', 1)])

    def test_multiple_elements_input(self):
        self.assertEqual(sort_counter({'a': 2, 'b': 3, 'c': 1}), [('b', 3), ('a', 2), ('c', 1)])

    def test_duplicates_input(self):
        self.assertEqual(sort_counter({'a': 2, 'b': 2, 'c': 1}), [('b', 2), ('a', 2), ('c', 1)])

    def test_empty_counter(self):
        self.assertEqual(sort_counter({'a': 0, 'b': 0, 'c': 0}), [])

    def test_counter_with_zero(self):
        self.assertEqual(sort_counter({'a': 0, 'b': 1, 'c': 0}), [('b', 1)])

    def test_counter_with_negative(self):
        self.assertEqual(sort_counter({'a': -1, 'b': 1, 'c': 0}), [('b', 1)])
