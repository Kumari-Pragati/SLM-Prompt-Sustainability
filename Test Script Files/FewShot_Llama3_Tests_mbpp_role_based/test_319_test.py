import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):
    def test_typical_use_case(self):
        text = "Hello world this is a test"
        expected_result = ["world", "test"]
        self.assertEqual(find_long_word(text), expected_result)

    def test_edge_case_empty_string(self):
        text = ""
        expected_result = []
        self.assertEqual(find_long_word(text), expected_result)

    def test_edge_case_single_word(self):
        text = "Hello"
        expected_result = ["Hello"]
        self.assertEqual(find_long_word(text), expected_result)

    def test_edge_case_multiple_words(self):
        text = "Hello world this is a test"
        expected_result = ["world", "test"]
        self.assertEqual(find_long_word(text), expected_result)

    def test_edge_case_non_alphanumeric_characters(self):
        text = "Hello! world this is a test"
        expected_result = ["world", "test"]
        self.assertEqual(find_long_word(text), expected_result)

    def test_edge_case_punctuation_at_end(self):
        text = "Hello world this is a test."
        expected_result = ["world", "test"]
        self.assertEqual(find_long_word(text), expected_result)

    def test_edge_case_punctuation_in_middle(self):
        text = "Hello world! this is a test"
        expected_result = ["world", "test"]
        self.assertEqual(find_long_word(text), expected_result)
