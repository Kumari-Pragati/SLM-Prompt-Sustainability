import unittest
from mbpp_565_code import split

class TestSplitFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(split(''), [])

    def test_single_character_string(self):
        self.assertEqual(split('a'), ['a'])

    def test_multiple_characters_string(self):
        self.assertEqual(split('abc'), ['a', 'b', 'c'])

    def test_string_with_spaces(self):
        self.assertEqual(split('hello world'), ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'])

    def test_string_with_special_characters(self):
        self.assertEqual(split('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '[', ']', '{', '}', '|', ';', ':', '\'', '<', '>', ',', '.', '?', '/'])

    def test_string_with_punctuation_at_start_and_end(self):
        self.assertEqual(split('.,;:!?'), ['.', ',', ';', ':', '!', '?'])

    def test_string_with_punctuation_in_middle(self):
        self.assertEqual(split('hello,world!'), ['h', 'e', 'l', 'l', 'o', ',', 'w', 'o', 'r', 'l', 'd', '!'])

    def test_string_with_only_punctuation(self):
        self.assertEqual(split('!!!?'), ['!', '!', '!', '?'])

    def test_string_with_empty_spaces(self):
        self.assertEqual(split('   '), [])
