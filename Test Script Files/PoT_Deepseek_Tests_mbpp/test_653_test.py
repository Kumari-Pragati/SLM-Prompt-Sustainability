import unittest
from mbpp_653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):

    def test_typical_case(self):
        data = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
        expected = {'a': [1, 2], 'b': [3, 4]}
        self.assertEqual(grouping_dictionary(data), expected)

    def test_empty_list(self):
        data = []
        expected = {}
        self.assertEqual(grouping_dictionary(data), expected)

    def test_single_element(self):
        data = [('a', 1)]
        expected = {'a': [1]}
        self.assertEqual(grouping_dictionary(data), expected)

    def test_duplicate_keys(self):
        data = [('a', 1), ('a', 2)]
        expected = {'a': [1, 2]}
        self.assertEqual(grouping_dictionary(data), expected)

    def test_invalid_input(self):
        data = [(1, 'a'), (2, 'b')]
        with self.assertRaises(TypeError):
            grouping_dictionary(data)
