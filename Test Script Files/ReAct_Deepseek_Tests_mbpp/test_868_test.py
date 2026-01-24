import unittest
from mbpp_868_code import length_Of_Last_Word

class TestLengthOfLastWord(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(length_Of_Last_Word("Hello World"), 5)

    def test_single_word(self):
        self.assertEqual(length_Of_Last_Word("Python"), 6)

    def test_empty_string(self):
        self.assertEqual(length_Of_Last_Word(""), 0)

    def test_spaces_only(self):
        self.assertEqual(length_Of_Last_Word("   "), 0)

    def test_single_space(self):
        self.assertEqual(length_Of_Last_Word(" "), 0)

    def test_multiple_spaces_between_words(self):
        self.assertEqual(length_Of_Last_Word("Hello   World"), 5)

    def test_trailing_spaces(self):
        self.assertEqual(length_Of_Last_Word("Hello World   "), 5)

    def test_single_character(self):
        self.assertEqual(length_Of_Last_Word("a"), 1)

    def test_multiple_characters(self):
        self.assertEqual(length_Of_Last_Word("abc"), 3)

    def test_mixed_case(self):
        self.assertEqual(length_Of_Last_Word("hElLo WoRlD"), 5)
