import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(capital_words_spaces("HelloWorld"), "Hello World")

    def test_edge_case_single_word(self):
        self.assertEqual(capital_words_spaces("Hello"), "Hello ")

    def test_edge_case_single_capital(self):
        self.assertEqual(capital_words_spaces("HeLLO"), "He LL O ")

    def test_edge_case_multiple_words(self):
        self.assertEqual(capital_words_spaces("HeLLoWoRlD"), "He LL o Wo Rl D")

    def test_edge_case_multiple_capitals(self):
        self.assertEqual(capital_words_spaces("HeLLoWoRlD123"), "He LL o Wo Rl D 123")

    def test_edge_case_empty_string(self):
        self.assertEqual(capital_words_spaces(""), "")

    def test_edge_case_only_numbers(self):
        self.assertEqual(capital_words_spaces("123456"), "123 456")

    def test_edge_case_only_special_characters(self):
        self.assertEqual(capital_words_spaces("!@#$%^&*()_+-="), "! @ # $ % ^ & * ( ) _ + - =")

    def test_edge_case_only_punctuation(self):
        self.assertEqual(capital_words_spaces(".,;:!?"), ", . ; : ! ? .")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            capital_words_spaces(123)
