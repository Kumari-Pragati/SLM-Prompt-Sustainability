import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_char_position(''), 0)

    def test_single_character_string(self):
        self.assertEqual(count_char_position('A'), 1)
        self.assertEqual(count_char_position('a'), 1)
        self.assertEqual(count_char_position('B'), 0)
        self.assertEqual(count_char_position('b'), 0)

    def test_multiple_characters_string(self):
        self.assertEqual(count_char_position('Abc'), 2)
        self.assertEqual(count_char_position('AbCd'), 3)
        self.assertEqual(count_char_position('AbCdEfGhIjKlMnOpQrStUvWxYz'), 26)
