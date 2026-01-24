import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyValue(unittest.TestCase):

    def test_typical_case(self):
        input_list = [('a', 1), ('b', 2), ('a', 3)]
        expected_output = {'a': [1, 3], 'b': [2]}
        self.assertEqual(group_keyvalue(input_list), expected_output)

    def test_empty_list(self):
        input_list = []
        expected_output = {}
        self.assertEqual(group_keyvalue(input_list), expected_output)

    def test_single_element(self):
        input_list = [('a', 1)]
        expected_output = {'a': [1]}
        self.assertEqual(group_keyvalue(input_list), expected_output)

    def test_duplicate_keys(self):
        input_list = [('a', 1), ('a', 2)]
        expected_output = {'a': [1, 2]}
        self.assertEqual(group_keyvalue(input_list), expected_output)

    def test_none_values(self):
        input_list = [('a', None), ('b', None)]
        expected_output = {'a': [None], 'b': [None]}
        self.assertEqual(group_keyvalue(input_list), expected_output)
