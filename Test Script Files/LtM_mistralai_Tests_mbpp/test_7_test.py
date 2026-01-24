import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):
    def test_simple_input(self):
        self.assertListEqual(find_char_long("HelloWorld"), ["Hello", "World"])

    def test_single_word(self):
        self.assertListEqual(find_char_long("Test"), ["Test"])

    def test_multiple_words(self):
        self.assertListEqual(find_char_long("ThisIsATest"), ["This", "Is", "Test"])

    def test_min_length(self):
        self.assertListEqual(find_char_long("abcd"), ["abcd"])

    def test_max_length(self):
        self.assertListEqual(find_char_long("abcdeabcdeabcde"), ["abcde", "abcde"])

    def test_empty_string(self):
        self.assertListEqual(find_char_long(""), [])

    def test_special_characters(self):
        self.assertListEqual(find_char_long("!HelloWorld@"), [])

    def test_punctuation_at_start_end(self):
        self.assertListEqual(find_char_long(".,;:!?HelloWorld.,;:!"), [])

    def test_punctuation_in_middle(self):
        self.assertListEqual(find_char_long("HelloWorld,,"), ["Hello", "World"])
