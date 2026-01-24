import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_single_word(self):
        self.assertEqual(snake_to_camel('word'), 'Word')

    def test_multiple_words(self):
        self.assertEqual(snake_to_camel('word1_word2'), 'Word1Word2')

    def test_leading_trailing_underscores(self):
        self.assertEqual(snake_to_camel('_word'), 'Word')
        self.assertEqual(snake_to_camel('word_'), 'Word')
        self.assertEqual(snake_to_camel('_word_'), 'Word')

    def test_leading_trailing_spaces(self):
        self.assertEqual(snake_to_camel(' word_word '), 'WordWord')
        self.assertEqual(snake_to_camel('_ word '), 'Word')
        self.assertEqual(snake_to_camel('_ word_'), 'Word')

    def test_multiple_consecutive_underscores(self):
        self.assertEqual(snake_to_camel('word__word'), 'WordWord')
        self.assertEqual(snake_to_camel('__word__'), '')

    def test_special_characters(self):
        self.assertEqual(snake_to_camel('word-word'), 'WordWord')
        self.assertEqual(snake_to_camel('word_123'), 'Word123')
        self.assertEqual(snake_to_camel('word_123_456'), 'Word123456')

    def test_empty_split_case(self):
        self.assertEqual(snake_to_camel(''), '')
        self.assertEqual(snake_to_camel(' '), '')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            snake_to_camel(123)
