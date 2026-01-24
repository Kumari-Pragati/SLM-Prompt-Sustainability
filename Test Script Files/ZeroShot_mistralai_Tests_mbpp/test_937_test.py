import unittest
from mbpp_937_code import Counter
from your_module import max_char  # Assuming the function is defined in a module named 'your_module'

class TestMaxChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(max_char(''), '')

    def test_single_character_string(self):
        self.assertEqual(max_char('a'), 'a')

    def test_multiple_characters_string(self):
        self.assertEqual(max_char('hello world'), 'l')

    def test_case_insensitive_string(self):
        self.assertEqual(max_char('HeLlO wOrLd'), 'l')

    def test_string_with_equal_characters(self):
        self.assertEqual(max_char('aaabbb'), 'b')

    def test_string_with_special_characters(self):
        self.assertEqual(max_char('Hello123World!'), 'H')
