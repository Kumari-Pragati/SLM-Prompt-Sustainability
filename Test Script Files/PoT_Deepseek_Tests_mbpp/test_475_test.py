import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_counter({'a': 3, 'b': 1, 'c': 2}), 
                         [('a', 3), ('c', 2), ('b', 1)])

    def test_empty_dict(self):
        self.assertEqual(sort_counter({}), [])

    def test_single_element(self):
        self.assertEqual(sort_counter({'a': 1}), [('a', 1)])

    def test_same_frequency(self):
        self.assertEqual(sort_counter({'a': 2, 'b': 2}), [('a', 2), ('b', 2)])

    def test_negative_values(self):
        self.assertEqual(sort_counter({'a': -1, 'b': -2}), [('b', -2), ('a', -1)])

    def test_large_numbers(self):
        self.assertEqual(sort_counter({'a': 1000, 'b': 2000}), [('b', 2000), ('a', 1000)])

    def test_non_integer_values(self):
        with self.assertRaises(TypeError):
            sort_counter({'a': '1', 'b': 2})
