import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):

    def test_typical_case(self):
        list = ['Hello', 'World']
        string = 'Hello, {}'
        expected_output = ['Hello, Hello', 'Hello, World']
        self.assertEqual(add_string(list, string), expected_output)

    def test_empty_list(self):
        list = []
        string = 'Hello, {}'
        expected_output = []
        self.assertEqual(add_string(list, string), expected_output)

    def test_single_element_list(self):
        list = ['Hello']
        string = 'Hello, {}'
        expected_output = ['Hello, Hello']
        self.assertEqual(add_string(list, string), expected_output)

    def test_string_without_format(self):
        list = ['Hello', 'World']
        string = 'Hello'
        expected_output = ['Hello', 'Hello']
        self.assertEqual(add_string(list, string), expected_output)

    def test_none_string(self):
        list = ['Hello', 'World']
        string = None
        with self.assertRaises(TypeError):
            add_string(list, string)
