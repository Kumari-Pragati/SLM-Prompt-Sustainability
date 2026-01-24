import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(first_repeated_word("apple banana apple"), "apple")

    def test_empty_string(self):
        self.assertEqual(first_repeated_word(""), 'None')

    def test_single_word(self):
        self.assertEqual(first_repeated_word("hello"), 'None')

    def test_no_repeated_word(self):
        self.assertEqual(first_repeated_word("apple banana orange"), 'None')

    def test_repeated_word_at_start(self):
        self.assertEqual(first_repeated_word("apple apple banana"), "apple")

    def test_repeated_word_at_end(self):
        self.assertEqual(first_repeated_word("apple banana banana"), "banana")

    def test_repeated_word_in_middle(self):
        self.assertEqual(first_repeated_word("apple banana banana apple"), "banana")

    def test_multiple_repeated_words(self):
        self.assertEqual(first_repeated_word("apple banana banana apple orange"), "banana")
