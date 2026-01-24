import unittest
from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")

    def test_edge_case_uppercase(self):
        self.assertEqual(camel_to_snake("HelloWorld"), "hello_world")

    def test_edge_case_lowercase(self):
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")

    def test_edge_case_empty_string(self):
        self.assertEqual(camel_to_snake(""), "")

    def test_edge_case_single_character(self):
        self.assertEqual(camel_to_snake("a"), "a")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(camel_to_snake("hello   world"), "hello_world")

    def test_edge_case_non_alphanumeric(self):
        self.assertEqual(camel_to_snake("hello!World"), "hello_world")

    def test_edge_case_multiple_camel_case(self):
        self.assertEqual(camel_to_snake("helloWorldThisIsACamelCase"), "hello_world_this_is_a_camel_case")

    def test_edge_case_camel_case_with_numbers(self):
        self.assertEqual(camel_to_snake("helloWorld123"), "hello_world_123")

    def test_edge_case_camel_case_with_underscores(self):
        self.assertEqual(camel_to_snake("hello_World"), "hello_world")

    def test_edge_case_camel_case_with_punctuation(self):
        self.assertEqual(camel_to_snake("helloWorld!"), "hello_world")

    def test_edge_case_camel_case_with_non_ascii(self):
        self.assertEqual(camel_to_snake("hëlloWorld"), "hëllo_world")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            camel_to_snake(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            camel_to_snake(None)
