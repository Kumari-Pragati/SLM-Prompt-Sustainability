import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(snake_to_camel("hello_world"), "HelloWorld")

    def test_edge_case_empty_string(self):
        self.assertEqual(snake_to_camel(""), "")

    def test_edge_case_single_word(self):
        self.assertEqual(snake_to_camel("hello"), "hello")

    def test_edge_case_no_underscores(self):
        self.assertEqual(snake_to_camel("hello"), "hello")

    def test_edge_case_multiple_underscores(self):
        self.assertEqual(snake_to_camel("hello___world"), "HelloWorld")

    def test_edge_case_leading_underscore(self):
        self.assertEqual(snake_to_camel("_hello_world"), "HelloWorld")

    def test_edge_case_trailing_underscore(self):
        self.assertEqual(snake_to_camel("hello_world_"), "HelloWorld")

    def test_edge_case_multiple_leading_underscores(self):
        self.assertEqual(snake_to_camel("__hello_world"), "HelloWorld")

    def test_edge_case_multiple_trailing_underscores(self):
        self.assertEqual(snake_to_camel("hello_world__"), "HelloWorld")
