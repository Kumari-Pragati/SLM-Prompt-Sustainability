import unittest
from mbpp_653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):

    def test_typical_case(self):
        l = [('a', 1), ('a', 2), ('b', 3)]
        expected_output = {'a': [1, 2], 'b': [3]}
        self.assertEqual(grouping_dictionary(l), expected_output)

    def test_empty_list(self):
        l = []
        expected_output = {}
        self.assertEqual(grouping_dictionary(l), expected_output)

    def test_single_element(self):
        l = [('a', 1)]
        expected_output = {'a': [1]}
        self.assertEqual(grouping_dictionary(l), expected_output)

    def test_duplicate_keys(self):
        l = [('a', 1), ('a', 2), ('a', 3)]
        expected_output = {'a': [1, 2, 3]}
        self.assertEqual(grouping_dictionary(l), expected_output)

    def test_invalid_input(self):
        l = [(1, 'a'), (2, 'b')]
        with self.assertRaises(TypeError):
            grouping_dictionary(l)
