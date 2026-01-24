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

    def test_spaces_and_words(self):
        self.assertEqual(length_Of_Last_Word("   Hello    World   "), 5)

    def test_single_space(self):
        self.assertEqual(length_Of_Last_Word(" "), 0)

    def test_single_space_and_word(self):
        self.assertEqual(length_Of_Last_Word("  Hello"), 5)

    def test_word_with_trailing_spaces(self):
        self.assertEqual(length_Of_Last_Word("Hello   "), 5)

    def test_word_with_leading_and_trailing_spaces(self):
        self.assertEqual(length_Of_Last_Word("   Hello   "), 5)

    def test_word_with_multiple_spaces(self):
        self.assertEqual(length_Of_Last_Word("Hello  World"), 5)
