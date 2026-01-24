import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):

    def test_simple_single_word(self):
        self.assertEqual(first_repeated_word("cat"), "cat")

    def test_simple_multiple_words(self):
        self.assertEqual(first_repeated_word("apple apple"), "apple")

    def test_simple_no_repeated_words(self):
        self.assertEqual(first_repeated_word("dog bird fish"), "None")

    def test_edge_case_empty_string(self):
        self.assertEqual(first_repeated_word(""), "None")

    def test_edge_case_single_space(self):
        self.assertEqual(first_repeated_word(" "), "None")

    def test_edge_case_whitespace_only(self):
        self.assertEqual(first_repeated_word("   \t\n\r"), "None")

    def test_edge_case_special_characters(self):
        self.assertEqual(first_repeated_word("!@#$%^&*()_+-=[]{}|;:'\",.<>/?"), "None")

    def test_edge_case_numbers(self):
        self.assertEqual(first_repeated_word("123 123"), "None")

    def test_edge_case_mixed_types(self):
        self.assertEqual(first_repeated_word("cat 123"), "None")
