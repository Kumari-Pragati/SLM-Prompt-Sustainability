import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):
    def test_typical_use_case(self):
        list_input = ['Hello', 'World']
        string_input = "{} is a test string"
        expected_output = ['Hello is a test string', 'World is a test string']
        self.assertEqual(add_string(list_input, string_input), expected_output)

    def test_edge_condition(self):
        list_input = []
        string_input = "{} is a test string"
        expected_output = []
        self.assertEqual(add_string(list_input, string_input), expected_output)

    def test_boundary_condition(self):
        list_input = ['Hello']
        string_input = "{} is a test string"
        expected_output = ['Hello is a test string']
        self.assertEqual(add_string(list_input, string_input), expected_output)

    def test_invalid_input(self):
        list_input = 'Hello'
        string_input = "{} is a test string"
        with self.assertRaises(TypeError):
            add_string(list_input, string_input)
