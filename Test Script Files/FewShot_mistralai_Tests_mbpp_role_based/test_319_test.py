import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):
    def test_find_long_word_with_five_letters(self):
        self.assertListEqual(find_long_word("This is a test"), ["test"])

    def test_find_long_word_with_more_than_five_letters(self):
        self.assertListEqual(find_long_word("This is a longer test"), [])

    def test_find_long_word_with_less_than_five_letters(self):
        self.assertListEqual(find_long_word("This is a"), [])

    def test_find_long_word_with_empty_string(self):
        self.assertListEqual(find_long_word(""), [])

    def test_find_long_word_with_special_characters(self):
        self.assertListEqual(find_long_word("This123is@a$test"), [])
