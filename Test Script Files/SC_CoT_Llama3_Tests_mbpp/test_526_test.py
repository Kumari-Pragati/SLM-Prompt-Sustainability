import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(capitalize_first_last_letters("hello world"), "He wOrld")

    def test_edge_case_empty_string(self):
        self.assertEqual(capitalize_first_last_letters(""), "")

    def test_edge_case_single_word(self):
        self.assertEqual(capitalize_first_last_letters("hello"), "hEllo")

    def test_edge_case_single_letter(self):
        self.assertEqual(capitalize_first_last_letters("a"), "a")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(capitalize_first_last_letters("   hello   world   "), "   He wOrld   ")

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            capitalize_first_last_letters(123)

    def test_edge_case_non_string_input_with_explicit_handling(self):
        self.assertEqual(capitalize_first_last_letters(None), "")
