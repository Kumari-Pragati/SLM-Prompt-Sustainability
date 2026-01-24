import unittest

from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):

    def test_typical_case(self):
        input_list = ['abc', 'defg', 'hij']
        expected_length, expected_list = 4, 'defg'
        self.assertEqual(max_length_list(input_list), (expected_length, expected_list))

    def test_edge_case_empty_list(self):
        input_list = []
        expected_length, expected_list = 0, ''
        self.assertEqual(max_length_list(input_list), (expected_length, expected_list))

    def test_edge_case_single_element(self):
        input_list = ['abc']
        expected_length, expected_list = 3, 'abc'
        self.assertEqual(max_length_list(input_list), (expected_length, expected_list))

    def test_corner_case_same_length_elements(self):
        input_list = ['abc', 'def', 'ghi']
        expected_length, expected_list = 3, 'abc'
        self.assertEqual(max_length_list(input_list), (expected_length, expected_list))

    def test_invalid_input_non_string_elements(self):
        input_list = [123, 'def', 456]
        with self.assertRaises(TypeError):
            max_length_list(input_list)
