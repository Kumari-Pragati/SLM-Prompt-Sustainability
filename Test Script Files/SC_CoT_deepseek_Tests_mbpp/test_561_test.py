import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):
    def test_typical_case(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        expected_output = {'a': [1], 'b': [2], 'c': [3]}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_duplicate_values(self):
        test_list = [('a', 1), ('b', 1), ('c', 3)]
        expected_output = {'a': [1], 'b': [1], 'c': [3]}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_duplicate_keys(self):
        test_list = [('a', 1), ('a', 2), ('c', 3)]
        expected_output = {'a': [1, 2], 'c': [3]}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = {}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_single_element(self):
        test_list = [('a', 1)]
        expected_output = {'a': [1]}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            assign_elements('invalid input')
