import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(capitalize_first_last_letters("hello world"), "Hello World")

    def test_single_word(self):
        self.assertEqual(capitalize_first_last_letters("world"), "World")

    def test_empty_string(self):
        self.assertEqual(capitalize_first_last_letters(""), "")

    def test_punctuation(self):
        self.assertEqual(capitalize_first_last_letters("Hello, World!"), "Hello, World!")

    def test_multiple_words_with_capital_letters(self):
        self.assertEqual(capitalize_first_last_letters("HeLlO wOrLd"), "HeLLo WoRld")

    def test_all_caps(self):
        self.assertEqual(capitalize_first_last_letters("HELLO WORLD"), "Hello World")

    def test_all_lowercase(self):
        self.assertEqual(capitalize_first_last_letters("hello world"), "Hello World")

    def test_all_small_letters_with_punctuation(self):
        self.assertEqual(capitalize_first_last_letters("h.e.l.l.o, w.o.r.l.d!"), "H.e.l.l.o, W.o.r.l.d!")
