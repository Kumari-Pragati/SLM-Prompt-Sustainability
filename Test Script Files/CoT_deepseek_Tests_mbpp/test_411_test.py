import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_single_word_snake_case(self):
        self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')

    def test_multiple_words_snake_case(self):
        self.assertEqual(snake_to_camel('multi_word_snake_case'), 'MultiWordSnakeCase')

    def test_already_camel_case(self):
        self.assertEqual(snake_to_camel('alreadyCamelCase'), 'AlreadyCamelCase')

    def test_empty_string(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_single_letter(self):
        self.assertEqual(snake_to_camel('a'), 'A')

    def test_all_lowercase(self):
        self.assertEqual(snake_to_camel('lowercase'), 'Lowercase')

    def test_all_uppercase(self):
        self.assertEqual(snake_to_camel('UPPERCASE'), 'Uppercase')

    def test_mixed_case(self):
        self.assertEqual(snake_to_camel('MiXeDcAsE'), 'Mixedcase')

    def test_with_numbers(self):
        self.assertEqual(snake_to_camel('with_numbers_123'), 'WithNumbers123')

    def test_with_special_characters(self):
        self.assertEqual(snake_to_camel('with_special_chars_!@#'), 'WithSpecialChars_!@#')
