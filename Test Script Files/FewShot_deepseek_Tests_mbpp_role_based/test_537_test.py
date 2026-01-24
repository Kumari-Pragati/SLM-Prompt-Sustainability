import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first_repeated_word('This is a test sentence with repeated words.'), 'is')

    def test_no_repeated_words(self):
        self.assertEqual(first_repeated_word('This is a unique sentence.'), 'None')

    def test_empty_string(self):
        self.assertEqual(first_repeated_word(''), 'None')

    def test_repeated_words_at_start(self):
        self.assertEqual(first_repeated_word('this is a test sentence with repeated words.'), 'is')

    def test_case_insensitive(self):
        self.assertEqual(first_repeated_word('This is a Test sentence with Repeated words.'), 'is')

    def test_multiple_spaces(self):
        self.assertEqual(first_repeated_word('This  is a test sentence with repeated words.'), 'is')
