import unittest
from mbpp_604_code import reverse_words

class TestReverseWords(unittest.TestCase):

    def test_empty_string(self):
        """Tests reversing an empty string"""
        self.assertEqual(reverse_words(''), '')

    def test_single_word(self):
        """Tests reversing a single word"""
        self.assertEqual(reverse_words('hello'), 'hello')

    def test_multiple_words(self):
        """Tests reversing multiple words"""
        self.assertEqual(reverse_words('hello world'), 'world hello')

    def test_whitespace_only(self):
        """Tests reversing whitespace only"""
        self.assertEqual(reverse_words('   '), '   ')

    def test_leading_trailing_whitespace(self):
        """Tests reversing a string with leading and trailing whitespace"""
        self.assertEqual(reverse_words('   hello   '), '   hello   ')

    def test_punctuation(self):
        """Tests reversing a string with punctuation"""
        self.assertEqual(reverse_words('hello, world!'), '! world, hello')

    def test_special_characters(self):
        """Tests reversing a string with special characters"""
        self.assertEqual(reverse_words('hello@world.com'), 'com.world@hello')

    def test_numbers(self):
        """Tests reversing a string with numbers"""
        self.assertEqual(reverse_words('123 hello 456'), '654 hello 321')

    def test_mixed_case(self):
        """Tests reversing a string with mixed case"""
        self.assertEqual(reverse_words('Hello World'), 'World Hello')

    def test_error_non_string(self):
        """Tests error handling for non-string input"""
        with self.assertRaises(TypeError):
            reverse_words(123)
