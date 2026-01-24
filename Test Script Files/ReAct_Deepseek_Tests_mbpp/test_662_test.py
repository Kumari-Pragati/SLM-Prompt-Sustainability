import unittest
from mbpp_662_code import sorted_dict

class TestSortedDict(unittest.TestCase):

    def test_typical_case(self):
        input_dict = {'a': [3, 2, 1], 'b': [4, 5, 6]}
        expected_output = {'a': [1, 2, 3], 'b': [4, 5, 6]}
        self.assertEqual(sorted_dict(input_dict), expected_output)

    def test_empty_dict(self):
        input_dict = {}
        expected_output = {}
        self.assertEqual(sorted_dict(input_dict), expected_output)

    def test_single_key_dict(self):
        input_dict = {'a': [3, 2, 1]}
        expected_output = {'a': [1, 2, 3]}
        self.assertEqual(sorted_dict(input_dict), expected_output)

    def test_duplicate_values(self):
        input_dict = {'a': [3, 2, 1, 2]}
        expected_output = {'a': [1, 2, 2, 3]}
        self.assertEqual(sorted_dict(input_dict), expected_output)

    def test_negative_numbers(self):
        input_dict = {'a': [-3, -2, -1]}
        expected_output = {'a': [-3, -2, -1]}
        self.assertEqual(sorted_dict(input_dict), expected_output)
