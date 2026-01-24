import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(remove_spaces(' '), ' ')
        self.assertEqual(remove_spaces('a '), 'a ')
        self.assertEqual(remove_spaces(' a'), 'a')

    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces('   a   b   c   '), 'a b c')

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_spaces(' a '), 'a')
        self.assertEqual(remove_spaces(' a\n\tb\n c '), 'a\nb\nc')

    def test_multiple_words(self):
        self.assertEqual(remove_spaces('a b c'), 'a b c')
        self.assertEqual(remove_spaces('a b c d'), 'a b c d')
        self.assertEqual(remove_spaces('a b c d e'), 'a b c d e')

    def test_punctuation(self):
        self.assertEqual(remove_spaces('a, b. c ! d?'), 'a,b.c!d?')
        self.assertEqual(remove_spaces('a, b. c ! d? "e" \'f\''), 'a,b.c!d?e\'f')

    def test_special_characters(self):
        self.assertEqual(remove_spaces('a_b@c#d$e^f&g*h(i)j+k-l~m'), 'a_bc@cd$e^fg&ghi+k-lm')
