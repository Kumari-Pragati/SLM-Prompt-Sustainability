import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyValue(unittest.TestCase):
    def test_typical_use_case(self):
        input_list = [('a', 1), ('b', 2), ('a', 3)]
        expected_output = {'a': [1, 3], 'b': [2]}
        self.assertEqual(group_keyvalue(input_list), expected_output)

    def test_edge_case_single_key(self):
        input_list = [('a', 1)]
        expected_output = {'a': [1]}
        self.assertEqual(group_keyvalue(input_list), expected_output)

    def test_boundary_case_empty_list(self):
        input_list = []
        expected_output = {}
        self.assertEqual(group_keyvalue(input_list), expected_output)

    def test_error_handling_invalid_input(self):
        input_list = [(1, 'a'), ('b', 2)]  # Invalid input, tuple elements are not strings
        with self.assertRaises(TypeError):
            group_keyvalue(input_list)
