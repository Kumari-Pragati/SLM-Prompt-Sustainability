import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_match_string('HelloWorld'), 'Found a match!')

    def test_empty_input(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_no_word_match(self):
        self.assertEqual(text_match_string('12345'), 'Not matched!')

    def test_match_with_spaces(self):
        self.assertEqual(text_match_string('Hello World'), 'Not matched!')

    def test_match_with_special_characters(self):
        self.assertEqual(text_match_string('Hello_World'), 'Not matched!')

    def test_match_with_numbers(self):
        self.assertEqual(text_match_string('Hello123World'), 'Not matched!')
