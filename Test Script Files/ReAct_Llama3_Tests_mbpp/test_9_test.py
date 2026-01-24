import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(find_Rotations(""), 0)

    def test_single_character_string(self):
        self.assertEqual(find_Rotations("a"), 1)

    def test_short_string(self):
        self.assertEqual(find_Rotations("abc"), 1)

    def test_long_string(self):
        self.assertEqual(find_Rotations("abcdefghijklmnopqrstuvwxyz"), 1)

    def test_rotated_string(self):
        self.assertEqual(find_Rotations("hellohello"), 5)

    def test_non_rotated_string(self):
        self.assertEqual(find_Rotations("abcdefg"), 7)

    def test_rotated_string_with_spaces(self):
        self.assertEqual(find_Rotations("hello worldhello world"), 5)

    def test_non_rotated_string_with_spaces(self):
        self.assertEqual(find_Rotations("abcdefg"), 7)
