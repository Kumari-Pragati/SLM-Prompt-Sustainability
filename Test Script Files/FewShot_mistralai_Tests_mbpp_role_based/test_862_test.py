import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):
    def test_typical_use_case(self):
        text = "This is a test sentence. This sentence has multiple words."
        expected_result = [('This', 2), ('is', 1), ('a', 1), ('test', 1), ('sentence', 1), ('has', 1), ('multiple', 1), ('words', 1)]
        self.assertEqual(n_common_words(text, 4), expected_result)

    def test_edge_case_single_word(self):
        text = "Hello"
        expected_result = [('Hello', 1)]
        self.assertEqual(n_common_words(text, 1), expected_result)

    def test_edge_case_no_words(self):
        text = ""
        expected_result = []
        self.assertEqual(n_common_words(text, 1), expected_result)

    def test_edge_case_non_alphabetic_characters(self):
        text = "1234567890!@#$%^&*()_+-=[]{}|;':\"<>,.?/"
        expected_result = []
        self.assertEqual(n_common_words(text, 0), expected_result)
