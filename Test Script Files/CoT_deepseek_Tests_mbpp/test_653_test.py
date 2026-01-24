import unittest
from mbpp_653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):

    def test_typical_case(self):
        input_list = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
        expected_output = {'a': [1, 3], 'b': [2, 4]}
        self.assertEqual(grouping_dictionary(input_list), expected_output)

    def test_empty_list(self):
        input_list = []
        expected_output = {}
        self.assertEqual(grouping_dictionary(input_list), expected_output)

    def test_single_element(self):
        input_list = [('a', 1)]
        expected_output = {'a': [1]}
        self.assertEqual(grouping_dictionary(input_list), expected_output)

    def test_duplicate_keys(self):
        input_list = [('a', 1), ('a', 2)]
        expected_output = {'a': [1, 2]}
        self.assertEqual(grouping_dictionary(input_list), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            grouping_dictionary('invalid input')
