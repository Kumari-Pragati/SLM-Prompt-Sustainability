import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):
    def test_typical_use_case(self):
        input_list = ['abc', 'defgh', 'ijkl']
        expected_length = 5
        expected_list = 'defgh'
        self.assertEqual(max_length_list(input_list), (expected_length, expected_list))

    def test_edge_case_empty_list(self):
        input_list = []
        expected_length = 0
        expected_list = ''
        self.assertEqual(max_length_list(input_list), (expected_length, expected_list))

    def test_boundary_case_single_element(self):
        input_list = ['abcdefgh']
        expected_length = 8
        expected_list = 'abcdefgh'
        self.assertEqual(max_length_list(input_list), (expected_length, expected_list))

    def test_boundary_case_same_length_elements(self):
        input_list = ['abc', 'def', 'ghi']
        expected_length = 3
        expected_list = 'abc'
        self.assertEqual(max_length_list(input_list), (expected_length, expected_list))

    def test_error_handling_non_string_elements(self):
        input_list = [123, 'defgh', 'ijkl']
        with self.assertRaises(TypeError):
            max_length_list(input_list)
