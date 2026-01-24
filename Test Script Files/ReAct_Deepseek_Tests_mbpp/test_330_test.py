import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):

    def test_typical_case(self):
        text = "This is a sample text with words of different lengths."
        expected_output = ['This', 'text', 'with', 'words', 'of', 'different', 'lengths']
        self.assertEqual(find_char(text), expected_output)

    def test_single_word(self):
        text = "Python"
        expected_output = ['Python']
        self.assertEqual(find_char(text), expected_output)

    def test_no_words(self):
        text = "1234567890"
        expected_output = []
        self.assertEqual(find_char(text), expected_output)

    def test_empty_string(self):
        text = ""
        expected_output = []
        self.assertEqual(find_char(text), expected_output)

    def test_special_characters(self):
        text = "!@#$%^&*()"
        expected_output = []
        self.assertEqual(find_char(text), expected_output)

    def test_whitespace_only(self):
        text = "   "
        expected_output = []
        self.assertEqual(find_char(text), expected_output)

    def test_mixed_case(self):
        text = "ThIs iS a tEst"
        expected_output = ['ThIs', 'iS', 'a', 'tEst']
        self.assertEqual(find_char(text), expected_output)

    def test_numbers_in_text(self):
        text = "12345 67890 123456"
        expected_output = ['12345', '67890', '123456']
        self.assertEqual(find_char(text), expected_output)
