import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(are_Rotations("waterbottle", "ottlewaterb"))
        self.assertTrue(are_Rotations("abcdefg", "gfedcba"))
        self.assertTrue(are_Rotations("abc", "cab"))

    def test_edge_cases(self):
        self.assertFalse(are_Rotations("", ""))
        self.assertFalse(are_Rotations("a", "b"))
        self.assertFalse(are_Rotations("waterbottle", "bottlewater"))
        self.assertFalse(are_Rotations("waterbottle", "waterbottle1"))

    def test_corner_cases(self):
        self.assertTrue(are_Rotations("a", "a"))
        self.assertTrue(are_Rotations("abcabc", "abcabc"))
        self.assertTrue(are_Rotations("abcabc", "abcabcabc"))
