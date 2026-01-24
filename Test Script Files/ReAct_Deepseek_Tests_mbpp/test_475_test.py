import unittest
from mbpp_475_code import sort_counter
from collections import Counter

class TestSortCounter(unittest.TestCase):

    def test_typical_case(self):
        input_dict = {'a': 3, 'b': 1, 'c': 2}
        expected_output = [('a', 3), ('c', 2), ('b', 1)]
        self.assertEqual(sort_counter(input_dict), expected_output)

    def test_empty_dict(self):
        input_dict = {}
        expected_output = []
        self.assertEqual(sort_counter(input_dict), expected_output)

    def test_single_element(self):
        input_dict = {'a': 1}
        expected_output = [('a', 1)]
        self.assertEqual(sort_counter(input_dict), expected_output)

    def test_same_frequency(self):
        input_dict = {'a': 2, 'b': 2}
        expected_output = [('a', 2), ('b', 2)]
        self.assertEqual(sort_counter(input_dict), expected_output)

    def test_negative_values(self):
        input_dict = {'a': -1, 'b': -2}
        expected_output = [('b', -2), ('a', -1)]
        self.assertEqual(sort_counter(input_dict), expected_output)

    def test_large_numbers(self):
        input_dict = {'a': 1000, 'b': 2000}
        expected_output = [('b', 2000), ('a', 1000)]
        self.assertEqual(sort_counter(input_dict), expected_output)
