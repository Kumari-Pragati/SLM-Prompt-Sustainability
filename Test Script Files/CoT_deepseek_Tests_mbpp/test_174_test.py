import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyValue(unittest.TestCase):
    
    def test_typical_case(self):
        input_list = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
        expected_output = {'a': [1, 3], 'b': [2, 4]}
        self.assertEqual(group_keyvalue(input_list), expected_output)
        
    def test_empty_list(self):
        input_list = []
        expected_output = {}
        self.assertEqual(group_keyvalue(input_list), expected_output)
        
    def test_single_key(self):
        input_list = [('a', 1), ('a', 2), ('a', 3)]
        expected_output = {'a': [1, 2, 3]}
        self.assertEqual(group_keyvalue(input_list), expected_output)
        
    def test_duplicate_keys(self):
        input_list = [('a', 1), ('b', 2), ('a', 3), ('b', 2)]
        expected_output = {'a': [1, 3], 'b': [2, 2]}
        self.assertEqual(group_keyvalue(input_list), expected_output)
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            group_keyvalue('invalid input')
