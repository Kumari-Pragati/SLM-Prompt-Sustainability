import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")

    def test_edge_case_uppercase(self):
        self.assertEqual(camel_to_snake("HELLO"), "hello")

    def test_edge_case_lowercase(self):
        self.assertEqual(camel_to_snake("hello"), "hello")

    def test_edge_case_empty_string(self):
        self.assertEqual(camel_to_snake(""), "")

    def test_edge_case_single_character(self):
        self.assertEqual(camel_to_snake("a"), "a")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(camel_to_snake("hello   world"), "hello_world")

    def test_edge_case_punctuation(self):
        self.assertEqual(camel_to_snake("hello!world"), "hello_world")

    def test_edge_case_numbers(self):
        self.assertEqual(camel_to_snake("hello123world"), "hello_123_world")

    def test_edge_case_special_characters(self):
        self.assertEqual(camel_to_snake("hello@world"), "hello_world")
