import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_single_word(self):
        self.assertEqual(snake_to_camel('word'), 'Word')

    def test_multiple_words(self):
        self.assertEqual(snake_to_camel('word1_word2'), 'word1Word2')

    def test_words_with_numbers(self):
        self.assertEqual(snake_to_camel('word1_2word'), 'word12word')

    def test_words_with_special_characters(self):
        self.assertEqual(snake_to_camel('word-with-hyphen'), 'wordWithHyphen')
        self.assertEqual(snake_to_camel('word_with_underscore'), 'wordWithUnderscore')

    def test_words_with_mixed_case(self):
        self.assertEqual(snake_to_camel('Word_with_Camel'), 'WordWithCamel')
        self.assertEqual(snake_to_camel('word_With_Camel'), 'wordWithCamel')

    def test_words_with_empty_spaces(self):
        self.assertEqual(snake_to_camel('word   with   spaces'), 'wordWithSpaces')
