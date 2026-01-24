import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(first_repeated_word(''), 'None')

    def test_single_word(self):
        self.assertEqual(first_repeated_word('apple'), 'None')

    def test_single_repeated_word(self):
        self.assertEqual(first_repeated_word('apple apple'), 'apple')

    def test_multiple_words(self):
        self.assertEqual(first_repeated_word('apple banana apple'), 'apple')

    def test_repeated_word_at_end(self):
        self.assertEqual(first_repeated_word('apple banana apple banana'), 'banana')

    def test_repeated_word_in_middle(self):
        self.assertEqual(first_repeated_word('apple banana apple banana apple'), 'apple')

    def test_repeated_word_case_insensitive(self):
        self.assertEqual(first_repeated_word('Apple Banana Apple Banana'), 'banana')

    def test_no_repeated_word(self):
        self.assertEqual(first_repeated_word('apple banana cherry'), 'None')
