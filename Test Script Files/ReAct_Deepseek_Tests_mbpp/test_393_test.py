import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):

    def test_typical_case(self):
        input_list = ['abc', 'defgh', 'ijklmn']
        expected_length, expected_list = 5, 'defgh'
        self.assertEqual(max_length_list(input_list), (expected_length, expected_list))

    def test_empty_list(self):
        input_list = []
        expected_length, expected_list = 0, ''
        self.assertEqual(max_length_list(input_list), (expected_length, expected_list))

    def test_list_with_single_element(self):
        input_list = ['abcdefgh']
        expected_length, expected_list = 8, 'abcdefgh'
        self.assertEqual(max_length_list(input_list), (expected_length, expected_list))

    def test_list_with_same_length_elements(self):
        input_list = ['abc', 'def', 'ghi']
        expected_length, expected_list = 3, 'abc'
        self.assertEqual(max_length_list(input_list), (expected_length, expected_list))

    def test_list_with_empty_string(self):
        input_list = ['abc', '', 'def']
        expected_length, expected_list = 3, 'abc'
        self.assertEqual(max_length_list(input_list), (expected_length, expected_list))

    def test_list_with_none_elements(self):
        with self.assertRaises(TypeError):
            max_length_list(['abc', None, 'def'])
