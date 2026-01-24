import unittest
from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):

    def test_equal_strings(self):
        self.assertEqual(check_Equality("hello"), "Equal")

    def test_not_equal_strings(self):
        self.assertEqual(check_Equality("hello world"), "Not Equal")

    def test_equal_strings_with_spaces(self):
        self.assertEqual(check_Equality("hello hello"), "Equal")

    def test_empty_string(self):
        self.assertEqual(check_Equality(""), "Equal")

    def test_single_character_string(self):
        self.assertEqual(check_Equality("a"), "Equal")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            check_Equality(123)

    def test_long_string(self):
        self.assertEqual(check_Equality("hello world hello world"), "Not Equal")

    def test_string_with_newline(self):
        self.assertEqual(check_Equality("hello\nworld"), "Not Equal")
