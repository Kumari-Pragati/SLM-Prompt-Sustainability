import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyvalue(unittest.TestCase):
    def test_typical_input(self):
        input_list = [('a', 1), ('b', 2), ('c', 3)]
        expected_output = {'a': [1], 'b': [2], 'c': [3]}
        self.assertEqual(group_keyvalue(input_list), expected_output)

    def test_edge_case_empty_input(self):
        input_list = []
        expected_output = {}
        self.assertEqual(group_keyvalue(input_list), expected_output)

    def test_edge_case_single_key(self):
        input_list = [('a', 1), ('a', 2)]
        expected_output = {'a': [1, 2]}
        self.assertEqual(group_keyvalue(input_list), expected_output)

    def test_edge_case_single_value(self):
        input_list = [('a', 1)]
        expected_output = {'a': [1]}
        self.assertEqual(group_keyvalue(input_list), expected_output)

    def test_edge_case_multiple_keys(self):
        input_list = [('a', 1), ('b', 2), ('c', 3)]
        expected_output = {'a': [1], 'b': [2], 'c': [3]}
        self.assertEqual(group_keyvalue(input_list), expected_output)

    def test_invalid_input_non_iterable(self):
        input_list = 'not a list'
        with self.assertRaises(TypeError):
            group_keyvalue(input_list)

    def test_invalid_input_non_tuple(self):
        input_list = [1, 2, 3]
        with self.assertRaises(TypeError):
            group_keyvalue(input_list)

    def test_invalid_input_non_iterable_non_tuple(self):
        input_list = 123
        with self.assertRaises(TypeError):
            group_keyvalue(input_list)
