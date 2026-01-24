import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):
    def test_typical_input(self):
        dict1 = {'a': 3, 'b': 2, 'c': 1}
        self.assertEqual(sort_counter(dict1), [('c', 1), ('b', 2), ('a', 3)])

    def test_edge_case(self):
        dict1 = {'a': 3, 'b': 2}
        self.assertEqual(sort_counter(dict1), [('a', 3), ('b', 2)])

    def test_empty_input(self):
        dict1 = {}
        self.assertEqual(sort_counter(dict1), [])

    def test_single_element_input(self):
        dict1 = {'a': 1}
        self.assertEqual(sort_counter(dict1), [('a', 1)])

    def test_negative_values_input(self):
        dict1 = {'a': 3, 'b': -2, 'c': 1}
        self.assertEqual(sort_counter(dict1), [('a', 3), ('c', 1), ('b', -2)])

    def test_non_integer_values_input(self):
        dict1 = {'a': 3.5, 'b': -2.2, 'c': 1.1}
        self.assertEqual(sort_counter(dict1), [('c', 1.1), ('a', 3.5), ('b', -2.2)])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            sort_counter('not a dictionary')
