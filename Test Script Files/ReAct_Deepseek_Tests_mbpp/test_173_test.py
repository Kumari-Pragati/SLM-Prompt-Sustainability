import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSpecialCharacters(unittest.TestCase):

    def test_remove_splchar_typical_case(self):
        text = "Hello, World!"
        expected_output = "HelloWorld"
        self.assertEqual(remove_splchar(text), expected_output)

    def test_remove_splchar_with_numbers(self):
        text = "123456"
        expected_output = "123456"
        self.assertEqual(remove_splchar(text), expected_output)

    def test_remove_splchar_with_special_characters(self):
        text = "@#$%^&*()"
        expected_output = ""
        self.assertEqual(remove_splchar(text), expected_output)

    def test_remove_splchar_with_whitespace(self):
        text = "   "
        expected_output = ""
        self.assertEqual(remove_splchar(text), expected_output)

    def test_remove_splchar_with_underscore(self):
        text = "hello_world"
        expected_output = "helloworld"
        self.assertEqual(remove_splchar(text), expected_output)

    def test_remove_splchar_empty_string(self):
        text = ""
        expected_output = ""
        self.assertEqual(remove_splchar(text), expected_output)
