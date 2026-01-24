import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):

    def test_simple_rotations(self):
        self.assertTrue(are_Rotations("waterbottle", "ottlewaterb"))
        self.assertTrue(are_Rotations("abcdefg", "gfedcba"))
        self.assertTrue(are_Rotations("abc", "cab"))

    def test_edge_cases(self):
        self.assertFalse(are_Rotations("", ""))
        self.assertFalse(are_Rotations("a", "b"))
        self.assertFalse(are_Rotations("waterbottle", "bottlewater"))
        self.assertFalse(are_Rotations("abcdefg", "defg"))
        self.assertFalse(are_Rotations("abcdefg", "abcdefgh"))

    def test_complex_cases(self):
        self.assertTrue(are_Rotations("practice", "icepract"))
        self.assertTrue(are_Rotations("stevens", "vensste"))
        self.assertFalse(are_Rotations("abcdefg", "xyz"))
        self.assertFalse(are_Rotations("waterbottle", "bottlewaterr"))
