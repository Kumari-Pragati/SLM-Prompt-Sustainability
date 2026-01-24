import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(capitalize_first_last_letters("hello world"), "Hel low WorlD")

    def test_edge_case_empty_string(self):
        self.assertEqual(capitalize_first_last_letters(""), "")

    def test_edge_case_single_word(self):
        self.assertEqual(capitalize_first_last_letters("hello"), "Hel")

    def test_edge_case_single_letter(self):
        self.assertEqual(capitalize_first_last_letters("a"), "a")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(capitalize_first_last_letters("   hello   world   "), "Hel low WorlD")

    def test_edge_case_punctuation(self):
        self.assertEqual(capitalize_first_last_letters("hello, world!"), "Hel, WorlD!")

    def test_edge_case_non_alpha_characters(self):
        self.assertEqual(capitalize_first_last_letters("hello123 world!"), "Hel low WorlD!")
