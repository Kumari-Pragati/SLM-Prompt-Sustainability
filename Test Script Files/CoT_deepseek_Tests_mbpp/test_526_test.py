import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):

    def test_capitalize_single_word(self):
        self.assertEqual(capitalize_first_last_letters('word'), 'Word')

    def test_capitalize_multiple_words(self):
        self.assertEqual(capitalize_first_last_letters('hello world'), 'Hello WorlD')

    def test_capitalize_already_capitalized(self):
        self.assertEqual(capitalize_first_last_letters('Hello World'), 'Hello World')

    def test_capitalize_empty_string(self):
        self.assertEqual(capitalize_first_last_letters(''), '')

    def test_capitalize_numbers_and_symbols(self):
        self.assertEqual(capitalize_first_last_letters('1234567890@#$%^&*()'), '1234567890@#$%^&*()')
