import unittest
from mbpp_482_code import match

class TestMatch(unittest.TestCase):
    def test_uppercase_and_lowercase_words(self):
        self.assertEqual(match('UppercaseAndLowercaseWords'), 'Yes')

    def test_all_uppercase_words(self):
        self.assertEqual(match('ALLUPPERCASEWORDS'), 'Yes')

    def test_all_lowercase_words(self):
        self.assertEqual(match('alllowercasewords'), 'Yes')

    def test_empty_string(self):
        self.assertEqual(match(''), 'No')

    def test_single_uppercase_letter(self):
        self.assertEqual(match('A'), 'No')

    def test_single_lowercase_letter(self):
        self.assertEqual(match('a'), 'No')

    def test_no_words(self):
        self.assertEqual(match('12345'), 'No')
