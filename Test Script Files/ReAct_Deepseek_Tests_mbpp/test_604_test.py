import unittest
from mbpp_604_code import reverse_words

class TestReverseWords(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(reverse_words('word'), 'word')

    def test_multiple_words(self):
        self.assertEqual(reverse_words('one two three'), 'three two one')

    def test_empty_string(self):
        self.assertEqual(reverse_words(''), '')

    def test_whitespace_only(self):
        self.assertEqual(reverse_words('   '), '   ')

    def test_single_character(self):
        self.assertEqual(reverse_words('a'), 'a')

    def test_special_characters(self):
        self.assertEqual(reverse_words('!@#$%^&*()'), '!@#$%^&*()')

    def test_numbers_in_words(self):
        self.assertEqual(reverse_words('123 456 789'), '789 456 123')

    def test_mixed_case(self):
        self.assertEqual(reverse_words('Hello WoRlD'), 'WoRlD Hello')

    def test_leading_trailing_whitespace(self):
        self.assertEqual(reverse_words('   leading   trailing   '), 'trailing   leading   ')
