import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(replace_spaces(''), '')

    def test_single_character(self):
        self.assertEqual(replace_spaces('a'), 'a')

    def test_multiple_characters(self):
        self.assertEqual(replace_spaces('abc'), 'a%b2c')

    def test_multiple_spaces(self):
        self.assertEqual(replace_spaces('hello world'), 'h%l%l%o%20w%o%r%l%d')

    def test_long_string(self):
        long_string = 'a' * 998 + ' ' + 'b' * 2
        self.assertEqual(replace_spaces(long_string), 'a' * 998 + '% ' + 'b' * 2)

    def test_string_longer_than_max(self):
        long_string = 'a' * (MAX + 1) + ' '
        self.assertEqual(replace_spaces(long_string), -1)

    def test_string_with_special_characters(self):
        self.assertEqual(replace_spaces('a%b c%d'), 'a%%b c%%d')
