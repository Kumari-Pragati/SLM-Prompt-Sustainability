import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_repeated_word('Hello world world'), 'world')

    def test_no_repeated_word(self):
        self.assertEqual(first_repeated_word('Hello world'), 'None')

    def test_repeated_word_at_the_end(self):
        self.assertEqual(first_repeated_word('Hello world world Hello'), 'world')

    def test_empty_string(self):
        self.assertEqual(first_repeated_word(''), 'None')

    def test_single_word(self):
        self.assertEqual(first_repeated_word('Hello'), 'None')

    def test_case_sensitivity(self):
        self.assertEqual(first_repeated_word('Hello World world'), 'None')

    def test_multiple_spaces(self):
        self.assertEqual(first_repeated_word('Hello   world world'), 'world')

    def test_special_characters(self):
        self.assertEqual(first_repeated_word('Hello world! world'), 'world')

    def test_numeric_words(self):
        self.assertEqual(first_repeated_word('1 2 1'), '1')
