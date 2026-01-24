import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(first_repeated_word("apple"), "apple")

    def test_no_repeated_words(self):
        self.assertEqual(first_repeated_word("banana bread"), "None")

    def test_repeated_first_word(self):
        self.assertEqual(first_repeated_word("apple apple"), "apple")

    def test_repeated_middle_word(self):
        self.assertEqual(first_repeated_word("apple banana apple"), "apple")

    def test_empty_string(self):
        self.assertEqual(first_repeated_word(""), "None")

    def test_single_space(self):
        self.assertEqual(first_repeated_word(" "), "None")

    def test_all_same_word(self):
        self.assertEqual(first_repeated_word("apple apple apple"), "apple")

    def test_all_different_words(self):
        self.assertEqual(first_repeated_word("apple banana cherry"), "None")
