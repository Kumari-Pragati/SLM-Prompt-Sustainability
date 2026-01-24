import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(first_repeated_word("apple apple"), "apple")

    def test_empty_input(self):
        self.assertEqual(first_repeated_word(""), 'None')

    def test_single_word_input(self):
        self.assertEqual(first_repeated_word("apple"), 'None')

    def test_no_repeated_word_input(self):
        self.assertEqual(first_repeated_word("apple banana"), 'None')

    def test_repeated_word_input(self):
        self.assertEqual(first_repeated_word("apple apple apple"), "apple")

    def test_multiple_repeated_word_input(self):
        self.assertEqual(first_repeated_word("apple apple banana banana"), "apple")

    def test_multiple_words_no_repeated_word_input(self):
        self.assertEqual(first_repeated_word("apple banana orange"), 'None')

    def test_multiple_words_with_repeated_word_input(self):
        self.assertEqual(first_repeated_word("apple apple banana orange"), "apple")
