import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):
    def test_normal_case(self):
        self.assertTrue(are_Rotations("water", "eratw"))
        self.assertTrue(are_Rotations("abcdefg", "gfedcba"))

    def test_edge_cases(self):
        self.assertTrue(are_Rotations("a", "a"))
        self.assertTrue(are_Rotations("abc", "cab"))
        self.assertFalse(are_Rotations("abc", "abcd"))
        self.assertFalse(are_Rotations("abc", "abcx"))

    def test_empty_strings(self):
        self.assertTrue(are_Rotations("", ""))
        self.assertFalse(are_Rotations("", "a"))

    def test_single_char_strings(self):
        self.assertTrue(are_Rotations("a", "a"))
        self.assertFalse(are_Rotations("a", "b"))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, are_Rotations, 1, 2)
        self.assertRaises(TypeError, are_Rotations, "1", 2)
        self.assertRaises(TypeError, are_Rotations, "1", "2")
