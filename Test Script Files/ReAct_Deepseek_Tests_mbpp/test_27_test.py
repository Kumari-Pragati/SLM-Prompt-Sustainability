import unittest
from mbpp_27_code import remove

class TestRemoveFunction(unittest.TestCase):

    def test_typical_case(self):
        input_list = ['abc123', 'def456']
        expected_output = ['abc', 'def']
        self.assertEqual(remove(input_list), expected_output)

    def test_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(remove(input_list), expected_output)

    def test_list_with_no_numbers(self):
        input_list = ['abc', 'def']
        expected_output = ['abc', 'def']
        self.assertEqual(remove(input_list), expected_output)

    def test_list_with_all_numbers(self):
        input_list = ['123', '456']
        expected_output = ['', '']
        self.assertEqual(remove(input_list), expected_output)

    def test_list_with_mixed_characters_and_numbers(self):
        input_list = ['abc123def', 'ghi456jkl']
        expected_output = ['abcdef', 'ghi456jkl']
        self.assertEqual(remove(input_list), expected_output)
