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
        self.assertEqual(snake_to_camel('word-1_2_word3'), 'word12Word3')

    def test_words_with_spaces(self):
        self.assertEqual(snake_to_camel('word 1_2_word3'), 'word12Word3')

    def test_words_with_capital_letters(self):
        self.assertEqual(snake_to_camel('Word_1_2_word3'), 'Word12Word3')

    def test_words_with_multiple_consecutive_underscores(self):
        self.assertEqual(snake_to_camel('word__1_2_word3'), 'word12Word3')
