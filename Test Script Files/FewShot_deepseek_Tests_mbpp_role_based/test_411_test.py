import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')

    def test_single_word(self):
        self.assertEqual(snake_to_camel('hello'), 'Hello')

    def test_empty_string(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_all_caps_snake_case(self):
        self.assertEqual(snake_to_camel('HELLO_WORLD'), 'HelloWorld')

    def test_no_underscore(self):
        self.assertEqual(snake_to_camel('helloworld'), 'Helloworld')

    def test_multiple_underscores(self):
        self.assertEqual(snake_to_camel('hello__world'), 'HelloWorld')

    def test_leading_underscore(self):
        self.assertEqual(snake_to_camel('_hello_world'), '_HelloWorld')

    def test_trailing_underscore(self):
        self.assertEqual(snake_to_camel('hello_world_'), 'HelloWorld_')

    def test_numeric_snake_case(self):
        self.assertEqual(snake_to_camel('hello_123'), 'Hello123')
