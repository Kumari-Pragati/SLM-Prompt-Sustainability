import unittest
from mbpp_507_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(remove_words([]), [])

    def test_single_word(self):
        self.assertListEqual(remove_words(["word"]), [])

    def test_multiple_words(self):
        self.assertListEqual(remove_words(["word1", "word2", "word3"]), ["word3"])

    def test_case_sensitivity(self):
        self.assertListEqual(remove_words(["Word1", "word2", "Word3"]), ["word2"])

    def test_multiple_removals(self):
        self.assertListEqual(remove_words(["word1", "word2", "word1", "word3"]), ["word2", "word1"])

    def test_empty_remove_words(self):
        self.assertListEqual(remove_words(["word1", "word2", "word3"], []), ["word1", "word2", "word3"])

    def test_non_existent_word(self):
        self.assertListEqual(remove_words(["word1", "word2", "word3"], ["not_a_word"]), ["word1", "word2", "word3"])

    def test_list_with_only_removals(self):
        self.assertListEqual(remove_words(["not_a_word"], ["not_a_word"]), [])

    def test_list_with_only_duplicates(self):
        self.assertListEqual(remove_words(["word", "word"], ["word"]), [])

    def test_list_with_duplicates_and_non_duplicates(self):
        self.assertListEqual(remove_words(["word1", "word2", "word1", "word3"], ["word1"]), ["word2", "word3"])
