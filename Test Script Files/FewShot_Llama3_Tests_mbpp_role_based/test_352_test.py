import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(unique_Characters(""))

    def test_single_character_string(self):
        self.assertTrue(unique_Characters("a"))

    def test_no_duplicates(self):
        self.assertTrue(unique_Characters("abcdefg"))

    def test_duplicates(self):
        self.assertFalse(unique_Characters("aabbcc"))

    def test_duplicates_at_end(self):
        self.assertFalse(unique_Characters("abcdefabc"))

    def test_duplicates_at_start(self):
        self.assertFalse(unique_Characters("abcabcabc"))

    def test_duplicates_in_middle(self):
        self.assertFalse(unique_Characters("abcdeabcde"))

    def test_duplicates_everywhere(self):
        self.assertFalse(unique_Characters("abcabcabcabc"))

    def test_duplicates_everywhere_reversed(self):
        self.assertFalse(unique_Characters("zyxwvutsrqponmlkjihgfedcba"))
