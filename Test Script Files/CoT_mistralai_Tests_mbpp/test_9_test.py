import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_Rotations(""), 1)

    def test_single_character(self):
        self.assertEqual(find_Rotations("a"), 1)

    def test_multiple_characters(self):
        self.assertEqual(find_Rotations("abc"), 1)

    def test_palindrome(self):
        self.assertEqual(find_Rotations("racecar"), 6)

    def test_longer_string(self):
        self.assertEqual(find_Rotations("abracadabra"), 11)

    def test_rotated_string(self):
        self.assertEqual(find_Rotations("waterbottle"), 10)

    def test_rotated_string_with_duplicates(self):
        self.assertEqual(find_Rotations("ppappp"), 4)

    def test_rotated_string_with_leading_spaces(self):
        self.assertEqual(find_Rotations("   waterbottle"), 10)

    def test_rotated_string_with_trailing_spaces(self):
        self.assertEqual(find_Rotations("waterbottle "), 10)

    def test_rotated_string_with_special_characters(self):
        self.assertEqual(find_Rotations("@waterbottle#"), 10)

    def test_rotated_string_with_numbers(self):
        self.assertEqual(find_Rotations("water1bottle2"), 10)

    def test_rotated_string_with_mixed_types(self):
        self.assertEqual(find_Rotations("water1bottle2@"), 10)

    def test_rotated_string_with_empty_string(self):
        self.assertEqual(find_Rotations("water@bottle"), 10)

    def test_rotated_string_with_multiple_rotations(self):
        self.assertEqual(find_Rotations("waterbottlewaterbottle"), 6)

    def test_rotated_string_with_long_rotation(self):
        self.assertEqual(find_Rotations("waterbottlewaterbottlewaterbottle"), 24)

    def test_rotated_string_with_short_rotation(self):
        self.assertEqual(find_Rotations("waterbottlewater"), 6)

    def test_rotated_string_with_no_rotation(self):
        self.assertEqual(find_Rotations("waterbottlewaterbottlewaterbottlewater"), None)
