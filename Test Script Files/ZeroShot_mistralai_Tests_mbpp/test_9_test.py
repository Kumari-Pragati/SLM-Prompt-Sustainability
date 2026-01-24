import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_Rotations(""), 0)

    def test_single_character(self):
        self.assertEqual(find_Rotations("a"), 1)

    def test_two_characters(self):
        self.assertEqual(find_Rotations("ab"), 1)

    def test_three_characters(self):
        self.assertEqual(find_Rotations("abc"), 1)

    def test_four_characters(self):
        self.assertEqual(find_Rotations("abcd"), 1)

    def test_longer_string(self):
        self.assertEqual(find_Rotations("abcdefg"), 6)

    def test_case_sensitivity(self):
        self.assertEqual(find_Rotations("ABC"), 1)

    def test_multiple_rotations(self):
        self.assertEqual(find_Rotations("abcabc"), 3)

    def test_no_rotations(self):
        self.assertEqual(find_Rotations("abcdefghij"), 11)
