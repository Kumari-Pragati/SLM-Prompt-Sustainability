import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):
    def test_strings_of_same_length(self):
        self.assertTrue(are_Rotations("hello", "ohell"))

    def test_strings_of_different_length(self):
        self.assertFalse(are_Rotations("hello", "world"))

    def test_strings_that_are_rotations(self):
        self.assertTrue(are_Rotations("abc", "cab"))

    def test_strings_that_are_not_rotations(self):
        self.assertFalse(are_Rotations("abc", "def"))

    def test_strings_with_spaces(self):
        self.assertTrue(are_Rotations("hello world", "world hello"))

    def test_strings_with_punctuation(self):
        self.assertTrue(are_Rotations("hello, world!", ", world! hello"))
