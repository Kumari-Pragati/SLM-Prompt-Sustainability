import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_single_word_snake_case(self):
        self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')

    def test_multiple_words_snake_case(self):
        self.assertEqual(snake_to_camel('python_is_fun'), 'PythonIsFun')

    def test_already_camel_case(self):
        self.assertEqual(snake_to_camel('PythonIsFun'), 'PythonIsFun')

    def test_empty_string(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_string_with_no_underscores(self):
        self.assertEqual(snake_to_camel('helloworld'), 'Helloworld')

    def test_string_with_underscores_at_start_and_end(self):
        self.assertEqual(snake_to_camel('_hello_world_'), 'HelloWorld')

    def test_string_with_underscores_only(self):
        self.assertEqual(snake_to_camel('____'), '')

    def test_string_with_numbers_and_underscores(self):
        self.assertEqual(snake_to_camel('hello_world_123'), 'HelloWorld123')
