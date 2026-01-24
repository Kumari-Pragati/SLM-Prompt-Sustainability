import unittest
from mbpp_653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):
    def test_typical_use_case(self):
        input_list = [('a', 1), ('a', 2), ('b', 3), ('c', 4)]
        expected_output = {'a': [1, 2], 'b': [3], 'c': [4]}
        self.assertEqual(grouping_dictionary(input_list), expected_output)

    def test_empty_input_list(self):
        input_list = []
        expected_output = defaultdict(list)
        self.assertEqual(grouping_dictionary(input_list), expected_output)

    def test_single_element_input_list(self):
        input_list = [('a', 1)]
        expected_output = {'a': [1]}
        self.assertEqual(grouping_dictionary(input_list), expected_output)

    def test_multiple_keys_with_same_value(self):
        input_list = [('a', 1), ('b', 1), ('c', 1)]
        expected_output = {'a': [1], 'b': [1], 'c': [1]}
        self.assertEqual(grouping_dictionary(input_list), expected_output)
