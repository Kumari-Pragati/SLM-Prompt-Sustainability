import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_single_word(self):
        self.assertEqual(snake_to_camel('word'), 'Word')

    def test_multiple_words(self):
        self.assertEqual(snake_to_camel('word1_word2'), 'word1Word2')

    def test_words_with_numbers(self):
        self.assertEqual(snake_to_camel('word1_2_word3'), 'word12Word3')

    def test_words_with_special_characters(self):
        self.assertEqual(snake_to_camel('word-with-hyphen'), 'wordWithHyphen')
        self.assertEqual(snake_to_camel('word_with_underscore'), 'wordWithUnderscore')

    def test_empty_word_in_middle(self):
        self.assertEqual(snake_to_camel('word_ _ word'), 'word Word word')

    def test_leading_trailing_whitespace(self):
        self.assertEqual(snake_to_camel(' _word_ '), 'Word')
        self.assertEqual(snake_to_camel(' word '), 'Word')
        self.assertEqual(snake_to_camel(' word_ '), 'Word')
        self.assertEqual(snake_to_camel(' _word '), 'Word')

    def test_all_uppercase(self):
        self.assertEqual(snake_to_camel('WORD'), 'Word')
        self.assertEqual(snake_to_camel('WORD_'), 'Word')
        self.assertEqual(snake_to_camel('_WORD'), 'Word')
        self.assertEqual(snake_to_camel('_WORD_'), 'Word')

    def test_all_lowercase(self):
        self.assertEqual(snake_to_camel('word'), 'Word')
        self.assertEqual(snake_to_camel('word_'), 'Word')
        self.assertEqual(snake_to_camel('_word'), 'Word')
        self.assertEqual(snake_to_camel('_word_'), 'Word')

    def test_invalid_input(self):
        self.assertRaises(TypeError, snake_to_camel, 123)
        self.assertRaises(TypeError, snake_to_camel, [])
        self.assertRaises(TypeError, snake_to_camel, None)
        self.assertRaises(TypeError, snake_to_camel, True)
        self.assertRaises(TypeError, snake_to_camel, False)
