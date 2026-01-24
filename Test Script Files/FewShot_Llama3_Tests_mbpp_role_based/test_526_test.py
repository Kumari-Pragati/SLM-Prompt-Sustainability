import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(capitalize_first_last_letters("hello world"), "HelLo WoRlD")

    def test_edge_case_empty_string(self):
        self.assertEqual(capitalize_first_last_letters(""), "")

    def test_edge_case_single_word(self):
        self.assertEqual(capitalize_first_last_letters("hello"), "hello")

    def test_edge_case_single_word_with_spaces(self):
        self.assertEqual(capitalize_first_last_letters("hello "), "hello ")

    def test_edge_case_multiple_words(self):
        self.assertEqual(capitalize_first_last_letters("hello world this is a test"), "HelLo WoRlD ThiS Is A TeSt")

    def test_edge_case_multiple_words_with_spaces(self):
        self.assertEqual(capitalize_first_last_letters("hello world this is a test with spaces"), "HelLo WoRlD ThiS Is A TeSt wItH SpAcEs")
