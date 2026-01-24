import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):

    def test_typical_case(self):
        input_list = ['abc', 'de', 'f']
        expected_length, expected_list = 2, 'de'
        self.assertEqual(min_length_list(input_list), (expected_length, expected_list))

    def test_edge_case(self):
        input_list = ['a', 'bc', 'def']
        expected_length, expected_list = 1, 'a'
        self.assertEqual(min_length_list(input_list), (expected_length, expected_list))

    def test_corner_case(self):
        input_list = ['', 'abc', 'def']
        expected_length, expected_list = 0, ''
        self.assertEqual(min_length_list(input_list), (expected_length, expected_list))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_length_list(123)
