import unittest
from mbpp_668_code import replace

class TestReplaceFunction(unittest.TestCase):

    def test_single_char_replacement(self):
        self.assertEqual(replace('hello', 'l'), 'helo')

    def test_multiple_consecutive_chars_replacement(self):
        self.assertEqual(replace('hellooo', 'o'), 'helo')

    def test_char_not_in_string(self):
        self.assertEqual(replace('hello', 'z'), 'hello')

    def test_empty_string(self):
        self.assertEqual(replace('', 'o'), '')

    def test_char_is_empty(self):
        self.assertEqual(replace('hello', ''), 'hello')

    def test_char_is_whitespace(self):
        self.assertEqual(replace('hello', ' '), 'hello')

    def test_special_characters(self):
        self.assertEqual(replace('hello!!', '!'), 'helo')

    def test_string_with_numbers(self):
        self.assertEqual(replace('hello111', '1'), 'helo')

    def test_string_with_special_characters_and_numbers(self):
        self.assertEqual(replace('hello!!111', '1'), 'helo')
