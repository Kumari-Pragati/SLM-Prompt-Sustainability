import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(odd_values_string(""), "")

    def test_single_character_string(self):
        self.assertEqual(odd_values_string("a"), "a")

    def test_even_length_string(self):
        self.assertEqual(odd_values_string("abcdef"), "ace")

    def test_odd_length_string(self):
        self.assertEqual(odd_values_string("abcdefg"), "aceg")

    def test_all_odd_characters(self):
        self.assertEqual(odd_values_string("13579"), "13579")

    def test_all_even_characters(self):
        self.assertEqual(odd_values_string("24680"), "")

    def test_mixed_characters(self):
        self.assertEqual(odd_values_string("13524680"), "135")

    def test_spaces_and_punctuation(self):
        self.assertEqual(odd_values_string("Hello, World!"), "Hlo")
