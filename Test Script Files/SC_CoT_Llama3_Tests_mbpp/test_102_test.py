import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(snake_to_camel("hello_world"), "helloWorld")

    def test_edge_case_empty_string(self):
        self.assertEqual(snake_to_camel(""), "")

    def test_edge_case_single_word(self):
        self.assertEqual(snake_to_camel("hello"), "hello")

    def test_edge_case_no_underscores(self):
        self.assertEqual(snake_to_camel("hello"), "hello")

    def test_edge_case_multiple_underscores(self):
        self.assertEqual(snake_to_camel("hello___world"), "helloWorld")

    def test_edge_case_leading_underscores(self):
        self.assertEqual(snake_to_camel("_hello_world"), "HelloWorld")

    def test_edge_case_trailing_underscores(self):
        self.assertEqual(snake_to_camel("hello_world_"), "helloWorld")

    def test_edge_case_multiple_leading_trailing_underscores(self):
        self.assertEqual(snake_to_camel("_hello___world_"), "HelloWorld")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            snake_to_camel(123)

    def test_invalid_input_non_string_list(self):
        with self.assertRaises(TypeError):
            snake_to_camel(["hello", "world"])
