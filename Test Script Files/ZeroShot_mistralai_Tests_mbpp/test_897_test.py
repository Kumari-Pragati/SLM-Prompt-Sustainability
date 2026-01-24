import unittest
from897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):

    def test_empty_sentence(self):
        self.assertFalse(is_Word_Present("", "word"))

    def test_single_word_sentence(self):
        self.assertTrue(is_Word_Present("word", "word"))
        self.assertFalse(is_Word_Present("notword", "word"))

    def test_multiple_words_sentence(self):
        self.assertTrue(is_Word_Present("word one word", "word"))
        self.assertTrue(is_Word_Present("word one word", "one"))
        self.assertFalse(is_Word_Present("word one word", "three"))

    def test_case_sensitivity(self):
        self.assertTrue(is_Word_Present("Word", "word"))
        self.assertFalse(is_Word_Present("word", "Word"))

    def test_punctuation(self):
        self.assertTrue(is_Word_Present("word, word", "word"))
        self.assertFalse(is_Word_Present("word, word", "comma"))
