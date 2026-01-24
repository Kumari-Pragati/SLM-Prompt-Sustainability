import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):

    def test_empty_sentence(self):
        self.assertFalse(is_Word_Present("", "word"))

    def test_single_word_sentence(self):
        self.assertTrue(is_Word_Present("word", "word"))
        self.assertFalse(is_Word_Present("notword", "word"))

    def test_multiple_words_sentence(self):
        self.assertTrue(is_Word_Present("first word second word", "second"))
        self.assertFalse(is_Word_Present("first word second word", "third"))

    def test_case_sensitivity(self):
        self.assertTrue(is_Word_Present("word", "Word"))
        self.assertFalse(is_Word_Present("Word", "word"))

    def test_whitespace_handling(self):
        self.assertTrue(is_Word_Present(" word   word  ", "word"))
        self.assertFalse(is_Word_Present(" word   notword  ", "notword"))

    def test_punctuation_handling(self):
        self.assertTrue(is_Word_Present("word, another word.", "word"))
        self.assertFalse(is_Word_Present("word, another word.", "another"))
