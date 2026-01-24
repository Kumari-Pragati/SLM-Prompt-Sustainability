import unittest
from mbpp_653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):

    def test_typical_case(self):
        l = [('a', 1), ('a', 2), ('b', 3)]
        expected = {'a': [1, 2], 'b': [3]}
        self.assertEqual(grouping_dictionary(l), expected)

    def test_empty_list(self):
        l = []
        expected = {}
        self.assertEqual(grouping_dictionary(l), expected)

    def test_single_element(self):
        l = [('a', 1)]
        expected = {'a': [1]}
        self.assertEqual(grouping_dictionary(l), expected)

    def test_duplicate_keys(self):
        l = [('a', 1), ('a', 2), ('a', 3)]
        expected = {'a': [1, 2, 3]}
        self.assertEqual(grouping_dictionary(l), expected)

    def test_mixed_types(self):
        l = [('a', 1), ('b', 'two'), ('c', True)]
        expected = {'a': [1], 'b': ['two'], 'c': [True]}
        self.assertEqual(grouping_dictionary(l), expected)
