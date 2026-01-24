import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):

    def test_typical_case(self):
        list_input = ['apple', 'banana', 'cherry']
        string_input = "I like {}"
        expected_output = ['I like apple', 'I like banana', 'I like cherry']
        self.assertEqual(add_string(list_input, string_input), expected_output)

    def test_empty_list(self):
        list_input = []
        string_input = "I like {}"
        expected_output = []
        self.assertEqual(add_string(list_input, string_input), expected_output)

    def test_single_element_list(self):
        list_input = ['apple']
        string_input = "I like {}"
        expected_output = ['I like apple']
        self.assertEqual(add_string(list_input, string_input), expected_output)

    def test_string_without_placeholder(self):
        list_input = ['apple', 'banana', 'cherry']
        string_input = "I like fruits"
        expected_output = ['I like fruits', 'I like fruits', 'I like fruits']
        self.assertEqual(add_string(list_input, string_input), expected_output)

    def test_invalid_input_type(self):
        list_input = 12345
        string_input = "I like {}"
        with self.assertRaises(TypeError):
            add_string(list_input, string_input)
