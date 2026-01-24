import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):
    def test_typical_case(self):
        test_list = [('key1', 'val1'), ('key2', 'val2'), ('key1', 'val3')]
        expected_output = {'key1': ['val1', 'val3'], 'key2': ['val2'], 'val1': [], 'val2': [], 'val3': []}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = {}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_single_element(self):
        test_list = [('key1', 'val1')]
        expected_output = {'key1': ['val1'], 'val1': []}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_duplicate_keys_and_values(self):
        test_list = [('key1', 'val1'), ('key1', 'val1')]
        expected_output = {'key1': ['val1', 'val1'], 'val1': []}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_invalid_input(self):
        test_list = [('key1', 'val1'), 'invalid_input']
        with self.assertRaises(TypeError):
            assign_elements(test_list)
