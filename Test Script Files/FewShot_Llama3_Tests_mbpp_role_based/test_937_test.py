import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_char("hello"), 'l')

    def test_empty_string(self):
        self.assertEqual(max_char(""), '')

    def test_single_character_string(self):
        self.assertEqual(max_char("a"), 'a')

    def test_multiple_characters_string(self):
        self.assertEqual(max_char("hello world"), 'l')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            max_char(123)

    def test_non_ascii_characters(self):
        self.assertEqual(max_char("hëllo"), 'l')
