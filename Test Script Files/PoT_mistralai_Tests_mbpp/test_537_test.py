import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_repeated_word("apple apple"), "apple")
        self.assertEqual(first_repeated_word("banana"), "None")
        self.assertEqual(first_repeated_word("apple banana apple"), "apple")

    def test_edge_case_single_word(self):
        self.assertEqual(first_repeated_word("apple"), "None")

    def test_edge_case_empty_string(self):
        self.assertEqual(first_repeated_word(""), "None")

    def test_edge_case_whitespace(self):
        self.assertEqual(first_repeated_word(" "), "None")

    def test_edge_case_multiple_repeated_words(self):
        self.assertEqual(first_repeated_word("apple apple banana apple"), "apple")

    def test_corner_case_case_insensitive(self):
        self.assertEqual(first_repeated_word("AppLe ApPlE aPpLe"), "AppLe")
