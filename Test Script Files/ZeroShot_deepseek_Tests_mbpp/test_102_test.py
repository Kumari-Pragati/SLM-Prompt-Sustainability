import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(snake_to_camel('hello'), 'Hello')

    def test_multiple_words(self):
        self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')

    def test_all_lowercase(self):
        self.assertEqual(snake_to_camel('lowercase_words'), 'LowercaseWords')

    def test_mixed_case(self):
        self.assertEqual(snake_to_camel('MiXeD_CaSe'), 'MixedCase')

    def test_empty_string(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_numbers_in_word(self):
        self.assertEqual(snake_to_camel('word_123'), 'Word123')

    def test_special_characters(self):
        self.assertEqual(snake_to_camel('special_chars!@#'), 'SpecialChars!@#')
