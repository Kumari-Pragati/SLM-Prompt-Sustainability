import unittest
from mbpp_668_code import re

def replace(string, char):
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string)
    return string

class TestReplaceFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(replace('', 'a'), '')

    def test_single_char(self):
        self.assertEqual(replace('a', 'a'), 'aa')

    def test_multiple_chars(self):
        self.assertEqual(replace('aa', 'a'), 'aaa')

    def test_string_with_multiple_repeated_chars(self):
        self.assertEqual(replace('aaaa', 'a'), 'aaaaa')

    def test_string_with_non_repeated_chars(self):
        self.assertEqual(replace('abcd', 'a'), 'abcd')

    def test_string_with_repeated_chars_and_non_repeated_chars(self):
        self.assertEqual(replace('aaabcd', 'a'), 'aaaabbbbccc')
