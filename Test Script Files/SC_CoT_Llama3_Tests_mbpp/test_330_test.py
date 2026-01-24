import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(find_char("Hello world, this is a test. It's a test of find_char function."), ['world', 'test', 'test'])

    def test_edge_case_empty_string(self):
        self.assertEqual(find_char(""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(find_char("Hello"), [])

    def test_edge_case_single_word_with_spaces(self):
        self.assertEqual(find_char("Hello world"), [])

    def test_edge_case_multiple_words(self):
        self.assertEqual(find_char("Hello world, this is a test. It's a test of find_char function. It's working fine."), ['world', 'this', 'test', 'test', 'fine'])

    def test_edge_case_multiple_words_with_punctuation(self):
        self.assertEqual(find_char("Hello world, this is a test. It's a test of find_char function. It's working fine. It's really cool!"), ['world', 'this', 'test', 'test', 'fine', 'cool'])

    def test_edge_case_multiple_words_with_punctuation_and_newline(self):
        self.assertEqual(find_char("Hello world, this is a test.\nIt's a test of find_char function.\nIt's working fine.\nIt's really cool!"), ['world', 'this', 'test', 'test', 'fine', 'cool'])

    def test_edge_case_multiple_words_with_punctuation_and_newline_and_tabs(self):
        self.assertEqual(find_char("Hello world, this is a test.\n\tIt's a test of find_char function.\n\tIt's working fine.\n\tIt's really cool!"), ['world', 'this', 'test', 'test', 'fine', 'cool'])

    def test_edge_case_multiple_words_with_punctuation_and_newline_and_tabs_and_spaces(self):
        self.assertEqual(find_char("Hello world, this is a test.\n\t\tIt's a test of find_char function.\n\t\tIt's working fine.\n\t\tIt's really cool!"), ['world', 'this', 'test', 'test', 'fine', 'cool'])
