import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):

    def test_typical_case(self):
        text = "This is a test sentence with long words like supercalifragilisticexpialidocious"
        expected_output = ['supercalifragilisticexpialidocious']
        self.assertEqual(find_long_word(text), expected_output)

    def test_no_long_words(self):
        text = "short words only"
        expected_output = []
        self.assertEqual(find_long_word(text), expected_output)

    def test_edge_case_single_long_word(self):
        text = "a" * 5
        expected_output = [text]
        self.assertEqual(find_long_word(text), expected_output)

    def test_edge_case_multiple_long_words(self):
        text = "a" * 5 + " " + "b" * 5
        expected_output = [("a" * 5), ("b" * 5)]
        self.assertEqual(find_long_word(text), expected_output)

    def test_edge_case_long_words_with_special_chars(self):
        text = "This is a test sentence with long words like supercalifragilisticexpialidocious!"
        expected_output = ['supercalifragilisticexpialidocious']
        self.assertEqual(find_long_word(text), expected_output)

    def test_error_case_empty_string(self):
        text = ""
        expected_output = []
        self.assertEqual(find_long_word(text), expected_output)
