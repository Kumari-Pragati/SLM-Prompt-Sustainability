import unittest
from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")

    def test_edge_case_uppercase(self):
        self.assertEqual(camel_to_snake("HelloWorld"), "hello_world")

    def test_edge_case_lowercase(self):
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")

    def test_edge_case_empty_string(self):
        self.assertEqual(camel_to_snake(""), "")

    def test_edge_case_single_word(self):
        self.assertEqual(camel_to_snake("hello"), "hello")

    def test_edge_case_single_uppercase(self):
        self.assertEqual(camel_to_snake("H"), "h")

    def test_edge_case_single_lowercase(self):
        self.assertEqual(camel_to_snake("h"), "h")

    def test_edge_case_multiple_uppercase(self):
        self.assertEqual(camel_to_snake("Hello"), "hello")

    def test_edge_case_multiple_lowercase(self):
        self.assertEqual(camel_to_snake("hello"), "hello")

    def test_edge_case_multiple_upper_and_lowercase(self):
        self.assertEqual(camel_to_snake("HelloWorld"), "hello_world")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(camel_to_snake("hello  world"), "hello_world")

    def test_edge_case_multiple_punctuation(self):
        self.assertEqual(camel_to_snake("hello!world"), "hello_world")

    def test_edge_case_multiple_digits(self):
        self.assertEqual(camel_to_snake("hello123world"), "hello_123_world")

    def test_edge_case_multiple_special_chars(self):
        self.assertEqual(camel_to_snake("hello@world"), "hello_world")
