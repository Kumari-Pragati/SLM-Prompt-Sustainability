import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUppercaseLowercase(unittest.TestCase):
    def test_uppercase_and_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('Hello World'), 'Found a match!')
        self.assertEqual(text_uppercase_lowercase('hello world'), 'Found a match!')

    def test_only_uppercase(self):
        self.assertEqual(text_uppercase_lowercase('ABCDEFG'), 'Found a match!')

    def test_only_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('abcdefg'), 'Found a match!')

    def test_empty_string(self):
        self.assertEqual(text_uppercase_lowercase(''), 'Not matched!')

    def test_single_uppercase(self):
        self.assertEqual(text_uppercase_lowercase('A'), 'Not matched!')

    def test_single_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('a'), 'Not matched!')

    def test_special_characters(self):
        self.assertEqual(text_uppercase_lowercase('Hello123World'), 'Not matched!')
