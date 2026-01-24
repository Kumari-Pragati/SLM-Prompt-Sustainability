import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")

    def test_edge_case_uppercase(self):
        self.assertEqual(camel_to_snake("HelloWorld"), "hello_world")

    def test_edge_case_lowercase(self):
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")

    def test_edge_case_empty_string(self):
        self.assertEqual(camel_to_snake(""), "")

    def test_edge_case_single_character(self):
        self.assertEqual(camel_to_snake("a"), "a")

    def test_edge_case_single_word(self):
        self.assertEqual(camel_to_snake("hello"), "hello")

    def test_edge_case_multiple_words(self):
        self.assertEqual(camel_to_snake("helloWorldGood"), "hello_world_good")

    def test_edge_case_non_alphanumeric(self):
        self.assertEqual(camel_to_snake("hello!World"), "hello_world")

    def test_edge_case_non_ascii(self):
        self.assertEqual(camel_to_snake("hëlloWörld"), "hëllo_wörld")
