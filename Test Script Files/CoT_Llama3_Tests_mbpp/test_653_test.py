import unittest
from mbpp_653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):
    def test_typical_input(self):
        input_list = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
        expected_output = {'a': [1, 2], 'b': [3, 4]}
        self.assertEqual(grouping_dictionary(input_list), expected_output)

    def test_edge_case_empty_input(self):
        input_list = []
        expected_output = defaultdict(list)
        self.assertEqual(grouping_dictionary(input_list), expected_output)

    def test_edge_case_single_key(self):
        input_list = [('a', 1)]
        expected_output = {'a': [1]}
        self.assertEqual(grouping_dictionary(input_list), expected_output)

    def test_edge_case_single_value(self):
        input_list = [('a', 1, 2)]
        expected_output = {'a': [1, 2]}
        self.assertEqual(grouping_dictionary(input_list), expected_output)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            grouping_dictionary('invalid_input')

    def test_invalid_input_structure(self):
        input_list = [1, 2, 3]
        with self.assertRaises(TypeError):
            grouping_dictionary(input_list)
