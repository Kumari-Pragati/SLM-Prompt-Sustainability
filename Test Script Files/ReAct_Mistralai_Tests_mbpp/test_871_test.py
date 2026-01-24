import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):

    def test_same_string(self):
        self.assertTrue(are_Rotations("abc", "abc"))

    def test_reverse_string(self):
        self.assertTrue(are_Rotations("abc", "cba"))

    def test_different_lengths(self):
        self.assertFalse(are_Rotations("abc", "abcd"))

    def test_empty_strings(self):
        self.assertTrue(are_Rotations("", ""))
        self.assertFalse(are_Rotations("", "a"))

    def test_single_char_strings(self):
        self.assertTrue(are_Rotations("a", "a"))
        self.assertFalse(are_Rotations("a", "b"))

    def test_case_sensitivity(self):
        self.assertFalse(are_Rotations("abc", "ABC"))
        self.assertTrue(are_Rotations("abc", "abc"))

    def test_whitespace(self):
        self.assertFalse(are_Rotations("abc ", "abc"))
        self.assertTrue(are_Rotations("abc", "abc "))
