import unittest
from mbpp_305_code import start_withp

class TestStartWithp(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(start_withp(["Pword1 Pword2"]), ("Pword1", "Pword2"))

    def test_empty_input(self):
        self.assertIsNone(start_withp([]))

    def test_single_word(self):
        self.assertIsNone(start_withp(["Pword1"]))

    def test_no_match(self):
        self.assertIsNone(start_withp(["word1 word2"]))

    def test_multiple_words(self):
        self.assertEqual(start_withp(["Pword1 Pword2", "Pword3 Pword4"]), ("Pword1", "Pword2"), ("Pword3", "Pword4"))

    def test_words_with_spaces(self):
        self.assertEqual(start_withp(["Pword1  Pword2", "Pword3   Pword4"]), ("Pword1", "Pword2"), ("Pword3", "Pword4"))

    def test_words_with_punctuation(self):
        self.assertEqual(start_withp(["Pword1, Pword2", "Pword3; Pword4"]), ("Pword1", "Pword2"), ("Pword3", "Pword4"))
