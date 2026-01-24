import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):

    def test_lowercase_string(self):
        self.assertTrue(is_lower("hello"))

    def test_mixed_case_string(self):
        self.assertTrue(is_lower("HeLlo"))

    def test_empty_string(self):
        self.assertTrue(is_lower(""))

    def test_whitespace_string(self):
        self.assertTrue(is_lower("\t\n "))

    def test_single_uppercase_letter(self):
        self.assertFalse(is_lower("A"))

    def test_multiple_uppercase_letters(self):
        self.assertFalse(is_lower("ABC"))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            is_lower(123)
