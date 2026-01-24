import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(capitalize_first_last_letters('hello world'), 'Hello WOrld')

    def test_single_word(self):
        self.assertEqual(capitalize_first_last_letters('python'), 'Python')

    def test_all_caps(self):
        self.assertEqual(capitalize_first_last_letters('HELLO WORLD'), 'HELLO WORLD')

    def test_all_lowercase(self):
        self.assertEqual(capitalize_first_last_letters('hello world'), 'Hello World')

    def test_empty_string(self):
        self.assertEqual(capitalize_first_last_letters(''), '')

    def test_numbers_in_string(self):
        self.assertEqual(capitalize_first_last_letters('123 hello 456'), '123 Hello 456')

    def test_special_characters(self):
        self.assertEqual(capitalize_first_last_letters('!hello@world#'), '!hello@world#')

    def test_special_case(self):
        self.assertEqual(capitalize_first_last_letters('a b c d'), 'A B C D')
