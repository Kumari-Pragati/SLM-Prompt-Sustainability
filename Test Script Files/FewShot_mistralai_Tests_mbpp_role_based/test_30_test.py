import unittest
from mbpp_30_code import count_Substring_WithEqualEnds

class TestCountSubstringWithEqualEnds(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_SubstringWithEqualEnds(''), 0)

    def test_single_character_string(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(count_SubstringWithEqualEnds(char), 1)

    def test_palindrome(self):
        self.assertEqual(count_SubstringWithEqualEnds('radar'), 1)
        self.assertEqual(count_SubstringWithEqualEnds('level'), 1)

    def test_non_palindrome(self):
        self.assertEqual(count_SubstringWithEqualEnds('hello'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('world'), 0)

    def test_mixed_case(self):
        self.assertEqual(count_SubstringWithEqualEnds('HeLLo'), 1)
        self.assertEqual(count_SubstringWithEqualEnds('WoRlD'), 0)

    def test_multi_word_sentence(self):
        self.assertEqual(count_SubstringWithEqualEnds('This is a test'), 0)
