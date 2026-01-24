import unittest
from mbpp_668_code import replace

class TestReplace(unittest.TestCase):

    def test_single_char(self):
        self.assertEqual(replace('hello', 'l'), 'helo')

    def test_multiple_chars(self):
        self.assertEqual(replace('hellllo', 'l'), 'helo')

    def test_char_not_in_string(self):
        self.assertEqual(replace('hello', 'z'), 'hello')

    def test_empty_string(self):
        self.assertEqual(replace('', 'l'), '')

    def test_string_with_special_chars(self):
        self.assertEqual(replace('hello!!', '!'), 'helo')

    def test_string_with_numbers(self):
        self.assertEqual(replace('hello111', '1'), 'helo')
