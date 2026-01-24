import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(snake_to_camel("hello_world"), "helloWorld")

    def test_empty_string(self):
        self.assertEqual(snake_to_camel(""), "")

    def test_single_word(self):
        self.assertEqual(snake_to_camel("hello"), "hello")

    def test_multiple_words(self):
        self.assertEqual(snake_to_camel("hello_world_foo"), "helloWorldFoo")

    def test_multiple_words_with_underscores(self):
        self.assertEqual(snake_to_camel("hello_world_foo_bar"), "helloWorldFooBar")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            snake_to_camel(123)
