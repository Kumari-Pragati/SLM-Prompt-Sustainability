import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_lowercase(''), '')

    def test_single_uppercase_letter(self):
        for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            self.assertEqual(remove_lowercase(char), char.upper())

    def test_single_uppercase_word(self):
        for word in ['HELLO', 'WORLD', 'PYTHON']:
            self.assertEqual(remove_lowercase(word), word.upper())

    def test_multiple_uppercase_words(self):
        for word in ['HELLO WORLD', 'PYTHON UNIT TEST', 'REACT STYLE LOOP']:
            self.assertEqual(remove_lowercase(word), word.upper().replace(' ', ''))

    def test_mixed_case_word(self):
        for word in ['MixedCaseWord', 'MiXeDcAsEwOrD']:
            self.assertEqual(remove_lowercase(word), word.upper().replace(' ', ''))

    def test_punctuation_and_numbers(self):
        for word in ['123abc', '!@#$%^&*()ABC', 'Hello, World!']:
            self.assertEqual(remove_lowercase(word), word.replace(' ', '').upper())

    def test_whitespace_only(self):
        self.assertEqual(remove_lowercase('   '), '')

    def test_unicode_string(self):
        unicode_string = 'Hello, 世界!'
        expected_result = unicode_string.upper().replace(' ', '')
        self.assertEqual(remove_lowercase(unicode_string), expected_result)

    def test_error_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_lowercase(123)
