import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(capitalize_first_last_letters('hello world'), 'Hello WOrld')

    def test_single_word(self):
        self.assertEqual(capitalize_first_last_letters('python'), 'Python')

    def test_all_caps_word(self):
        self.assertEqual(capitalize_first_last_letters('HELLO'), 'HELLO')

    def test_all_lowercase_word(self):
        self.assertEqual(capitalize_first_last_letters('hello'), 'Hello')

    def test_empty_string(self):
        self.assertEqual(capitalize_first_last_letters(''), '')

    def test_special_characters(self):
        self.assertEqual(capitalize_first_last_letters('!@#$%^&*()'), '!@#$%^&*()')

    def test_numbers_in_string(self):
        self.assertEqual(capitalize_first_last_letters('1234567890'), '1234567890')

    def test_whitespace_only(self):
        self.assertEqual(capitalize_first_last_letters('   '), '   ')
