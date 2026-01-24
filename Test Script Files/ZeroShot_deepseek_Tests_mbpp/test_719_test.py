import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_single_character(self):
        self.assertEqual(text_match('a'), 'Found a match!')
        self.assertEqual(text_match('b'), 'Not matched!')

    def test_multiple_characters(self):
        self.assertEqual(text_match('aa'), 'Found a match!')
        self.assertEqual(text_match('ab'), 'Found a match!')
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_asterisk(self):
        self.assertEqual(text_match('aaa'), 'Found a match!')
        self.assertEqual(text_match('aab'), 'Found a match!')
        self.assertEqual(text_match('abb'), 'Not matched!')
