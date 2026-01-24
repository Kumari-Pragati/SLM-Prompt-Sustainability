import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):
    def test_empty_string(self):
        self.assertIsNone(first_non_repeating_character(''))

    def test_single_character(self):
        self.assertEqual(first_non_repeating_character('a'), 'a')

    def test_repeated_characters(self):
        self.assertIsNone(first_non_repeating_character('aa'))

    def test_multiple_characters(self):
        self.assertEqual(first_non_repeating_character('abc'), 'a')

    def test_long_string(self):
        self.assertEqual(first_non_repeating_character('abcdefghijklmnopqrstuvwxyz'), 'a')

    def test_mixed_case(self):
        self.assertEqual(first_non_repeating_character('AbCdEfGhIjKlMnOpQrStUvWxYz'), 'A')

    def test_repeated_at_end(self):
        self.assertIsNone(first_non_repeating_character('abcabc'))

    def test_repeated_in_middle(self):
        self.assertIsNone(first_non_repeating_character('abba'))

    def test_repeated_at_beginning(self):
        self.assertIsNone(first_non_repeating_character('aaa'))

    def test_invalid_input_empty_list(self):
        with self.assertRaises(TypeError):
            first_non_repeating_character([])

    def test_invalid_input_integer(self):
        with self.assertRaises(TypeError):
            first_non_repeating_character(123)
