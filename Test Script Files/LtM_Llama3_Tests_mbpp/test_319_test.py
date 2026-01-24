import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(find_long_word(""), [])

    def test_single_word(self):
        self.assertEqual(find_long_word("hello"), [])

    def test_multiple_words(self):
        self.assertEqual(find_long_word("hello world"), [])

    def test_long_word(self):
        self.assertEqual(find_long_word("hello world helloagain"), ["helloagain"])

    def test_multiple_long_words(self):
        self.assertEqual(find_long_word("hello world helloagain goodbyeworld"), ["helloagain", "goodbyeworld"])

    def test_edge_case(self):
        self.assertEqual(find_long_word("hello world helloagain goodbyeworld helloagainagain"), ["helloagain", "goodbyeworld", "helloagainagain"])

    def test_non_word_characters(self):
        self.assertEqual(find_long_word("hello! world"), [])

    def test_non_word_characters_and_spaces(self):
        self.assertEqual(find_long_word("hello! world, goodbyeworld"), [])
