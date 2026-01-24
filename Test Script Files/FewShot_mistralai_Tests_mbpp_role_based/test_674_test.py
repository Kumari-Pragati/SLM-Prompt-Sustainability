import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(remove_duplicate("hello"), "hello")

    def test_multiple_words(self):
        self.assertEqual(remove_duplicate("hello world"), "hello world")

    def test_duplicate_words(self):
        self.assertEqual(remove_duplicate("hello hello"), "hello")

    def test_empty_string(self):
        self.assertEqual(remove_duplicate(""), "")

    def test_whitespace_only(self):
        self.assertEqual(remove_duplicate("   "), "")

    def test_punctuation(self):
        self.assertEqual(remove_duplicate("hello,world!"), "hello world")

    def test_mixed_case(self):
        self.assertEqual(remove_duplicate("Hello World"), "Hello World")
