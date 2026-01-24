import unittest
from mbpp_897_code import is_Word_Present

class TestIsWordPresent(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_Word_Present("Hello World", "World"))

    def test_edge_case_empty_sentence(self):
        self.assertFalse(is_Word_Present("", "World"))

    def test_edge_case_empty_word(self):
        self.assertFalse(is_Word_Present("Hello World", ""))

    def test_edge_case_sentence_with_spaces(self):
        self.assertTrue(is_Word_Present("   Hello   World   ", "World"))

    def test_edge_case_word_with_spaces(self):
        self.assertTrue(is_Word_Present("Hello World", "  World  "))

    def test_edge_case_sentence_with_punctuation(self):
        self.assertTrue(is_Word_Present("Hello, World!", "World"))

    def test_edge_case_word_with_punctuation(self):
        self.assertTrue(is_Word_Present("Hello, World!", ",World"))

    def test_edge_case_sentence_with_numbers(self):
        self.assertTrue(is_Word_Present("Hello 123 World", "World"))

    def test_edge_case_word_with_numbers(self):
        self.assertTrue(is_Word_Present("Hello 123 World", "123World"))

    def test_edge_case_sentence_with_special_chars(self):
        self.assertTrue(is_Word_Present("Hello!@# World", "World"))

    def test_edge_case_word_with_special_chars(self):
        self.assertTrue(is_Word_Present("Hello!@# World", "!@#World"))

    def test_edge_case_sentence_with_newlines(self):
        self.assertTrue(is_Word_Present("Hello\nWorld", "World"))

    def test_edge_case_word_with_newlines(self):
        self.assertTrue(is_Word_Present("Hello\nWorld", "\nWorld"))

    def test_edge_case_sentence_with_tabs(self):
        self.assertTrue(is_Word_Present("Hello\tWorld", "World"))

    def test_edge_case_word_with_tabs(self):
        self.assertTrue(is_Word_Present("Hello\tWorld", "\tWorld"))

    def test_edge_case_sentence_with_multiple_spaces(self):
        self.assertTrue(is_Word_Present("Hello   World   ", "World"))

    def test_edge_case_word_with_multiple_spaces(self):
        self.assertTrue(is_Word_Present("Hello   World   ", "   World   "))

    def test_edge_case_sentence_with_multiple_punctuation(self):
        self.assertTrue(is_Word_Present("Hello,.,!@# World", "World"))

    def test_edge_case_word_with_multiple_punctuation(self):
        self.assertTrue(is_Word_Present("Hello,.,!@# World", ",.,!@#World"))

    def test_edge_case_sentence_with_multiple_numbers(self):
        self.assertTrue(is_Word_Present("Hello 123 456 World", "World"))

    def test_edge_case_word_with_multiple_numbers(self):
        self.assertTrue(is_Word_Present("Hello 123 456 World", "123 456World"))

    def test_edge_case_sentence_with_multiple_special_chars(self):
        self.assertTrue(is_Word_Present("Hello!@# $%^&* World", "World"))

    def test_edge_case_word_with_multiple_special_chars(self):
        self.assertTrue(is_Word_Present("Hello!@# $%^&* World", "!@#$%^&*World"))

    def test_edge_case_sentence_with_newlines_and_spaces(self):
        self.assertTrue(is_Word_Present("Hello\n   World   ", "World"))

    def test_edge_case_word_with_newlines_and_spaces(self):
        self.assertTrue(is_Word_Present("Hello\n   World   ", "\n   World   "))

    def test_edge_case_sentence_with_tabs_and_spaces(self):
        self.assertTrue(is_Word_Present("Hello\t   World   ", "World"))

    def test_edge_case_word_with_tabs_and_spaces(self):
        self.assertTrue(is_Word_Present("Hello\t   World   ", "\t   World   "))

    def test_edge_case_sentence_with_newlines_and_punctuation(self):
        self.assertTrue(is_Word_Present("Hello,\n!@# World", "World"))

    def test_edge_case_word_with_newlines_and_punctuation(self):
        self.assertTrue(is_Word_Present("Hello,\n!@# World", ",\n!@#World"))

    def test_edge_case_sentence_with_tabs_and_punctuation(self):
        self.assertTrue(is_Word_Present("Hello,\t!@# World", "World"))

    def test_edge_case_word_with_tabs_and_punctuation(self):
        self.assertTrue(is_Word_Present("Hello,\t!@# World", ",\t!@#World"))

    def test_edge_case_sentence_with_newlines_and_numbers(self):
        self.assertTrue(is_Word_Present("Hello 123\n456 World", "World"))

    def test_edge_case_word_with_newlines_and_numbers(self):
        self.assertTrue(is_Word_Present("Hello 123\n456 World", "123\n456World"))

    def test_edge_case_sentence_with_tabs_and_numbers(self):
        self.assertTrue(is_Word_Present("Hello 123\t456 World", "World"))

    def