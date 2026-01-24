import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(unique_Characters(''))

    def test_single_character_string(self):
        self.assertTrue(unique_Characters('a'))

    def test_all_unique_characters(self):
        self.assertTrue(unique_Characters('abcde'))

    def test_repeating_characters(self):
        self.assertFalse(unique_Characters('aabbcc'))

    def test_repeating_characters_at_the_end(self):
        self.assertFalse(unique_Characters('abcdeabcde'))

    def test_repeating_characters_at_the_start(self):
        self.assertFalse(unique_Characters('abcdeabcde'))

    def test_repeating_characters_at_the_middle(self):
        self.assertFalse(unique_Characters('abcdeabcde'))

    def test_repeating_characters_at_the_start_and_end(self):
        self.assertFalse(unique_Characters('abcdeabcde'))

    def test_repeating_characters_at_the_start_and_middle(self):
        self.assertFalse(unique_Characters('abcdeabcde'))

    def test_repeating_characters_at_the_end_and_middle(self):
        self.assertFalse(unique_Characters('abcdeabcde'))

    def test_repeating_characters_at_the_start_and_end_and_middle(self):
        self.assertFalse(unique_Characters('abcdeabcde'))
