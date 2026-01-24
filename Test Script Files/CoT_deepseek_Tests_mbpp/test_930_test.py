import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match('ab'), 'Found a match!')
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('abb'), 'Found a match!')
        self.assertEqual(text_match('abbb'), 'Found a match!')

    def test_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_single_character_string(self):
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('b'), 'Not matched!')

    def test_multiple_characters_string(self):
        self.assertEqual(text_match('ababab'), 'Found a match!')
        self.assertEqual(text_match('abababab'), 'Found a match!')

    def test_none_input(self):
        with self.assertRaises(TypeError):
            text_match(None)
