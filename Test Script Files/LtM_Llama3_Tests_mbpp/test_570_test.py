import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_words(["hello world", "python is fun"], ["world", "python"]), ["hello is fun"])

    def test_empty_input(self):
        self.assertEqual(remove_words([], ["world", "python"]), [])

    def test_empty_charlist(self):
        self.assertEqual(remove_words(["hello world", "python is fun"], []), ["hello world", "python is fun"])

    def test_single_word(self):
        self.assertEqual(remove_words(["hello", "world"], ["world"]), ["hello"])

    def test_multiple_words(self):
        self.assertEqual(remove_words(["hello world", "python is fun", "programming is cool"], ["world", "python", "cool"]), ["hello is fun", "programming is"])

    def test_multiple_lines(self):
        self.assertEqual(remove_words(["hello world", "python is fun", "programming is cool"], ["world", "python", "cool"]), ["hello is fun", "programming is"])

    def test_empty_line(self):
        self.assertEqual(remove_words(["", "hello world", "python is fun"], ["world", "python"]), ["", "hello is fun"])

    def test_multiple_charlists(self):
        self.assertEqual(remove_words(["hello world", "python is fun", "programming is cool"], [["world", "python"], ["cool", "fun"]]), ["hello is fun", "programming is"])
