import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):

    def test_are_Rotations_true(self):
        self.assertTrue(are_Rotations("abc", "cab"))

    def test_are_Rotations_false(self):
        self.assertFalse(are_Rotations("abc", "def"))

    def test_are_Rotations_same_string(self):
        self.assertTrue(are_Rotations("abc", "abc"))

    def test_are_Rotations_empty_string(self):
        self.assertFalse(are_Rotations("", ""))

    def test_are_Rotations_single_character(self):
        self.assertTrue(are_Rotations("a", "a"))

    def test_are_Rotations_single_character_false(self):
        self.assertFalse(are_Rotations("a", "b"))

    def test_are_Rotations_rotations_of_empty_string(self):
        self.assertTrue(are_Rotations("", ""))
