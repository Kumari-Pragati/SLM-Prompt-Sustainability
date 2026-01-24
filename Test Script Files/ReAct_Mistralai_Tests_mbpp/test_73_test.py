import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(multiple_split(''), [])

    def test_single_space(self):
        self.assertEqual(multiple_split(' a '), ['a'])

    def test_single_char(self):
        self.assertEqual(multiple_split('a'), ['a'])

    def test_single_word(self):
        self.assertEqual(multiple_split('Hello'), ['Hello'])

    def test_multiple_words(self):
        self.assertEqual(multiple_split('Hello World'), ['Hello', 'World'])

    def test_multiple_words_with_punctuation(self):
        self.assertEqual(multiple_split('Hello, World!'), ['Hello', 'World'])

    def test_multiple_words_with_newline(self):
        self.assertEqual(multiple_split('Hello\nWorld'), ['Hello', 'World'])

    def test_multiple_words_with_special_characters(self):
        self.assertEqual(multiple_split('Hello*World'), ['Hello', 'World'])

    def test_multiple_words_with_semicolon(self):
        self.assertEqual(multiple_split('Hello;World'), ['Hello', 'World'])

    def test_multiple_words_with_comma_and_semicolon(self):
        self.assertEqual(multiple_split('Hello, World; Goodbye'), ['Hello', 'World', 'Goodbye'])

    def test_multiple_words_with_newline_and_semicolon(self):
        self.assertEqual(multiple_split('Hello\nWorld; Goodbye'), ['Hello', 'World', 'Goodbye'])

    def test_multiple_words_with_newline_comma_and_semicolon(self):
        self.assertEqual(multiple_split('Hello\nWorld, Goodbye; Hello Again'), ['Hello', 'World', 'Goodbye', 'Hello Again'])

    def test_multiple_words_with_special_characters_and_newline(self):
        self.assertEqual(multiple_split('Hello*World\nGoodbye'), ['Hello', 'World', 'Goodbye'])

    def test_multiple_words_with_special_characters_and_semicolon(self):
        self.assertEqual(multiple_split('Hello*World; Goodbye'), ['Hello', 'World', 'Goodbye'])

    def test_multiple_words_with_special_characters_and_comma(self):
        self.assertEqual(multiple_split('Hello*World, Goodbye'), ['Hello', 'World', 'Goodbye'])

    def test_multiple_words_with_special_characters_and_newline_comma(self):
        self.assertEqual(multiple_split('Hello*World\n, Goodbye'), ['Hello', 'World', 'Goodbye'])

    def test_multiple_words_with_special_characters_and_newline_semicolon(self):
        self.assertEqual(multiple_split('Hello*World\n; Goodbye'), ['Hello', 'World', 'Goodbye'])

    def test_multiple_words_with_special_characters_and_newline_comma_semicolon(self):
        self.assertEqual(multiple_split('Hello*World\n, Goodbye; Hello Again'), ['Hello', 'World', 'Goodbye', 'Hello Again'])

    def test_empty_list_input(self):
        with self.assertRaises(ValueError):
            multiple_split([])

    def test_none_input(self):
        with self.assertRaises(TypeError):
            multiple_split(None)
