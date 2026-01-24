import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):
    def test_simple_rotations(self):
        self.assertTrue(are_Rotations("abc", "cab"))
        self.assertTrue(are_Rotations("xyz", "yzx"))
        self.assertTrue(are_Rotations("abc", "bca"))

    def test_edge_rotations(self):
        self.assertFalse(are_Rotations("a", "b"))
        self.assertFalse(are_Rotations("a", "a"))
        self.assertFalse(are_Rotations("", ""))

    def test_rotations_with_same_string(self):
        self.assertTrue(are_Rotations("abc", "abc"))

    def test_rotations_with_empty_strings(self):
        self.assertFalse(are_Rotations("", "abc"))
        self.assertFalse(are_Rotations("abc", ""))

    def test_rotations_with_non_rotations(self):
        self.assertFalse(are_Rotations("abc", "def"))
