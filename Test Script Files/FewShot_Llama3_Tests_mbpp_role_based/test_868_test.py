import unittest
from mbpp_868_code import length_Of_Last_Word

class TestLengthOfLastWord(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(length_Of_Last_Word(""), 0)

    def test_single_word(self):
        self.assertEqual(length_Of_Last_Word("hello"), 5)

    def test_multiple_words(self):
        self.assertEqual(length_Of_Last_Word("hello world"), 5)

    def test_multiple_spaces(self):
        self.assertEqual(length_Of_Last_Word("   hello   "), 5)

    def test_leading_spaces(self):
        self.assertEqual(length_Of_Last_Word("   hello"), 5)

    def test_trailing_spaces(self):
        self.assertEqual(length_Of_Last_Word("hello   "), 5)

    def test_multiple_spaces_between_words(self):
        self.assertEqual(length_Of_Last_Word("hello  world"), 5)
