import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(multiple_split(''), [])

    def test_single_char(self):
        self.assertEqual(multiple_split('a'), ['a'])

    def test_single_word(self):
        self.assertEqual(multiple_split('hello'), ['hello'])

    def test_multiple_words(self):
        self.assertEqual(multiple_split('hello world'), ['hello', 'world'])

    def test_multiple_words_with_spaces(self):
        self.assertEqual(multiple_split('hello   world'), ['hello', 'world'])

    def test_multiple_words_with_punctuation(self):
        self.assertEqual(multiple_split('hello, world!'), ['hello', 'world'])

    def test_multiple_words_with_newline(self):
        self.assertEqual(multiple_split('hello\nworld'), ['hello', 'world'])

    def test_multiple_words_with_special_characters(self):
        self.assertEqual(multiple_split('hello*world'), ['hello', 'world'])

    def test_multiple_words_with_multiple_delimiters(self):
        self.assertEqual(multiple_split('hello; world,*world'), ['hello', 'world', 'world'])

    def test_escaped_delimiter(self):
        self.assertEqual(multiple_split('hello;world'), ['hello;world'])

    def test_empty_delimiter(self):
        self.assertEqual(multiple_split(';'), [])

    def test_invalid_input(self):
        self.assertRaises(TypeError, multiple_split, 123)
