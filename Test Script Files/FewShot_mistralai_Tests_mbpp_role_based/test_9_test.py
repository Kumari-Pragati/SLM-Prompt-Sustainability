import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):
    def test_single_character_string(self):
        self.assertEqual(find_Rotations("a"), 1)

    def test_two_character_string(self):
        self.assertEqual(find_Rotations("ab"), 1)

    def test_longer_string(self):
        self.assertEqual(find_Rotations("abcdefg"), 7)

    def test_empty_string(self):
        self.assertEqual(find_Rotations(""), 0)

    def test_string_with_duplicates(self):
        self.assertEqual(find_Rotations("aa"), 1)

    def test_string_with_special_characters(self):
        self.assertEqual(find_Rotations("!@#$%^&*()ABCDEFG"), 15)

    def test_string_with_whitespace(self):
        self.assertEqual(find_Rotations("Hello World"), 11)

    def test_string_with_multiple_rotations(self):
        self.assertEqual(find_Rotations("abcdefgabcdefg"), 6)

    def test_string_with_no_rotations(self):
        self.assertEqual(find_Rotations("xyz"), 3)
