import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first_repeated_word("hello world hello"), "hello")

    def test_edge_case_empty_string(self):
        self.assertEqual(first_repeated_word(""), 'None')

    def test_edge_case_single_word(self):
        self.assertEqual(first_repeated_word("hello"), 'None')

    def test_edge_case_no_repeated_word(self):
        self.assertEqual(first_repeated_word("hello world"), 'None')

    def test_edge_case_multiple_repeated_words(self):
        self.assertEqual(first_repeated_word("hello world hello again hello"), "hello")

    def test_edge_case_empty_string_with_spaces(self):
        self.assertEqual(first_repeated_word("   "), 'None')

    def test_edge_case_single_word_with_spaces(self):
        self.assertEqual(first_repeated_word("   hello   "), 'None')

    def test_edge_case_no_repeated_word_with_spaces(self):
        self.assertEqual(first_repeated_word("   hello world   "), 'None')

    def test_edge_case_multiple_repeated_words_with_spaces(self):
        self.assertEqual(first_repeated_word("   hello world hello again hello   "), "hello")
