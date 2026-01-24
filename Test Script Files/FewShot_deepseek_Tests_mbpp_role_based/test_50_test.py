import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):
    def test_typical_use_case(self):
        input_list = ['hello', 'world', 'python']
        expected_output = (5, 'python')
        self.assertEqual(min_length_list(input_list), expected_output)

    def test_edge_case_empty_list(self):
        input_list = []
        expected_output = (0, '')
        self.assertEqual(min_length_list(input_list), expected_output)

    def test_boundary_case_single_element(self):
        input_list = ['single']
        expected_output = (6, 'single')
        self.assertEqual(min_length_list(input_list), expected_output)

    def test_boundary_case_empty_string(self):
        input_list = ['', 'hello', 'world']
        expected_output = (0, '')
        self.assertEqual(min_length_list(input_list), expected_output)

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            min_length_list(123)
