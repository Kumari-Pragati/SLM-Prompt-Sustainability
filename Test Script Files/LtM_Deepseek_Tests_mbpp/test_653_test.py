import unittest
from mbpp_653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):

    def test_simple_input(self):
        l = [('a', 1), ('b', 2), ('a', 3)]
        expected_output = {'a': [1, 3], 'b': [2]}
        self.assertEqual(grouping_dictionary(l), expected_output)

    def test_empty_input(self):
        l = []
        expected_output = {}
        self.assertEqual(grouping_dictionary(l), expected_output)

    def test_single_element_input(self):
        l = [('a', 1)]
        expected_output = {'a': [1]}
        self.assertEqual(grouping_dictionary(l), expected_output)

    def test_duplicate_keys(self):
        l = [('a', 1), ('a', 2)]
        expected_output = {'a': [1, 2]}
        self.assertEqual(grouping_dictionary(l), expected_output)

    def test_mixed_types(self):
        l = [(1, 'a'), (2, 'b')]
        expected_output = {1: ['a'], 2: ['b']}
        self.assertEqual(grouping_dictionary(l), expected_output)
