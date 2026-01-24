import unittest
from mbpp_604_code import reverse_words

class TestReverseWords(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(reverse_words('Hello World'), 'World Hello')

    def test_single_word(self):
        self.assertEqual(reverse_words('Python'), 'Python')

    def test_empty_string(self):
        self.assertEqual(reverse_words(''), '')

    def test_multiple_spaces(self):
        self.assertEqual(reverse_words('Hello     World'), 'World Hello')

    def test_special_characters(self):
        self.assertEqual(reverse_words('Hello, World!'), 'World! Hello,')

    def test_numbers_in_words(self):
        self.assertEqual(reverse_words('123 456'), '456 123')

    def test_special_characters_and_numbers(self):
        self.assertEqual(reverse_words('Hello, 123!'), '123! Hello,')

    def test_special_characters_and_spaces(self):
        self.assertEqual(reverse_words('Hello@World'), 'World@Hello')
