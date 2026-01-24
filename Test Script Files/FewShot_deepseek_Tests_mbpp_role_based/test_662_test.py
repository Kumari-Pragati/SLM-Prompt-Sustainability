import unittest
from mbpp_662_code import sorted_dict

class TestSortedDict(unittest.TestCase):
    def test_typical_use_case(self):
        input_dict = {'a': [3, 2, 1], 'b': [4, 5, 6]}
        expected_output = {'a': [1, 2, 3], 'b': [4, 5, 6]}
        self.assertEqual(sorted_dict(input_dict), expected_output)

    def test_edge_case_empty_dict(self):
        input_dict = {}
        expected_output = {}
        self.assertEqual(sorted_dict(input_dict), expected_output)

    def test_boundary_case_single_item(self):
        input_dict = {'a': [3]}
        expected_output = {'a': [3]}
        self.assertEqual(sorted_dict(input_dict), expected_output)

    def test_boundary_case_duplicate_values(self):
        input_dict = {'a': [3, 3]}
        expected_output = {'a': [3, 3]}
        self.assertEqual(sorted_dict(input_dict), expected_output)

    def test_error_handling_non_list_values(self):
        input_dict = {'a': 'not a list'}
        with self.assertRaises(TypeError):
            sorted_dict(input_dict)
