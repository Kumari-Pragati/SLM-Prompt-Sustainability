import unittest
from mbpp_653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):
    def test_typical_input(self):
        input_list = [('a', 1), ('a', 2), ('b', 3), ('c', 4)]
        expected_output = {'a': [1, 2], 'b': [3], 'c': [4]}
        self.assertEqual(grouping_dictionary(input_list), expected_output)

    def test_edge_case_empty_input(self):
        input_list = []
        expected_output = {}
        self.assertEqual(grouping_dictionary(input_list), expected_output)

    def test_edge_case_single_element_input(self):
        input_list = [('a', 1)]
        expected_output = {'a': [1]}
        self.assertEqual(grouping_dictionary(input_list), expected_output)

    def test_edge_case_single_element_input_empty_value(self):
        input_list = [('a', None)]
        expected_output = {'a': [None]}
        self.assertEqual(grouping_dictionary(input_list), expected_output)

    def test_edge_case_single_element_input_non_hashable_key(self):
        input_list = [(1, 1)]
        with self.assertRaises(TypeError):
            grouping_dictionary(input_list)

    def test_edge_case_non_list_input(self):
        input_list = {'a': [1, 2]}
        with self.assertRaises(TypeError):
            grouping_dictionary(input_list)

    def test_edge_case_non_iterable_input(self):
        input_list = 123
        with self.assertRaises(TypeError):
            grouping_dictionary(input_list)
