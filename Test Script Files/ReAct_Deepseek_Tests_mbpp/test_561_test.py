import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('key1', 'val1'), ('key2', 'val2'), ('key1', 'val3')]
        expected_result = {'key1': ['val1', 'val3'], 'key2': ['val2']}
        self.assertEqual(assign_elements(test_list), expected_result)

    def test_empty_list(self):
        test_list = []
        expected_result = {}
        self.assertEqual(assign_elements(test_list), expected_result)

    def test_single_element(self):
        test_list = [('key1', 'val1')]
        expected_result = {'key1': ['val1']}
        self.assertEqual(assign_elements(test_list), expected_result)

    def test_duplicate_values(self):
        test_list = [('key1', 'val1'), ('key2', 'val1')]
        expected_result = {'key1': ['val1'], 'key2': ['val1']}
        self.assertEqual(assign_elements(test_list), expected_result)

    def test_duplicate_keys(self):
        test_list = [('key1', 'val1'), ('key1', 'val2')]
        expected_result = {'key1': ['val1', 'val2']}
        self.assertEqual(assign_elements(test_list), expected_result)

    def test_empty_keys_and_values(self):
        test_list = [(None, None), (None, None)]
        expected_result = {None: [None, None]}
        self.assertEqual(assign_elements(test_list), expected_result)
