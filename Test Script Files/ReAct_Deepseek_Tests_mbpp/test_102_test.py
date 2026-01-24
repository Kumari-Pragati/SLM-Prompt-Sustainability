import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_single_word_snake_case(self):
        self.assertEqual(snake_to_camel('hello'), 'Hello')

    def test_multiple_words_snake_case(self):
        self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')

    def test_already_camel_case(self):
        self.assertEqual(snake_to_camel('HelloWorld'), 'HelloWorld')

    def test_empty_string(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_single_letter_snake_case(self):
        self.assertEqual(snake_to_camel('h'), 'H')

    def test_snake_case_with_numbers(self):
        self.assertEqual(snake_to_camel('hello_123'), 'Hello123')

    def test_snake_case_with_special_characters(self):
        self.assertEqual(snake_to_camel('hello_world_!@#'), 'HelloWorld!@#')

    def test_snake_case_with_mixed_case(self):
        self.assertEqual(snake_to_camel('HeLLo_WoRlD'), 'HeLLoWoRlD')
