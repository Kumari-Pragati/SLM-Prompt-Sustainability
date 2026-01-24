import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_char_position(''), 0)

    def test_single_letter(self):
        for char in 'ABCabc':
            self.assertEqual(count_char_position(char), 1)

    def test_multiple_letters(self):
        for string in ('AAA', 'AaBbCc', 'abcdefghijklmnopqrstuvwxyz'):
            self.assertEqual(count_char_position(string), len(string))

    def test_mixed_case(self):
        self.assertEqual(count_char_position('AaBbCc'), 3)
        self.assertEqual(count_char_position('aAbBcC'), 3)

    def test_non_alphabetic_characters(self):
        for string in ('123', '!@#$%^&*()', 'ABC123'):
            self.assertEqual(count_char_position(string), 0)

    def test_whitespace(self):
        for string in (' ', '   ', 'A B C', 'A   B   C'):
            self.assertEqual(count_char_position(string), 0)
