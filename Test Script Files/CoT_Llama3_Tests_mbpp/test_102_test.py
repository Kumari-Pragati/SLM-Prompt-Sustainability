import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):
    def test_typical_snake_case(self):
        self.assertEqual(snake_to_camel("hello_world"), "HelloWorld")

    def test_multiple_underscores(self):
        self.assertEqual(snake_to_camel("hello_world_foo"), "HelloWorldFoo")

    def test_single_word(self):
        self.assertEqual(snake_to_camel("hello"), "hello")

    def test_empty_string(self):
        self.assertEqual(snake_to_camel(""), "")

    def test_single_character(self):
        self.assertEqual(snake_to_camel("a"), "a")

    def test_no_underscores(self):
        self.assertEqual(snake_to_camel("hello"), "hello")

    def test_leading_underscore(self):
        self.assertEqual(snake_to_camel("_hello_world"), "HelloWorld")

    def test_trailing_underscore(self):
        self.assertEqual(snake_to_camel("hello_world_"), "HelloWorld")

    def test_multiple_leading_underscores(self):
        self.assertEqual(snake_to_camel("__hello_world"), "HelloWorld")

    def test_multiple_trailing_underscores(self):
        self.assertEqual(snake_to_camel("hello_world__"), "HelloWorld")

    def test_multiple_leading_and_trailing_underscores(self):
        self.assertEqual(snake_to_camel("__hello_world__"), "HelloWorld")
