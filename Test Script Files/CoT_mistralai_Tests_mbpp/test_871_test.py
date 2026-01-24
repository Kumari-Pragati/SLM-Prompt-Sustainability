import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):
    def test_same_string(self):
        self.assertTrue(are_Rotations('abc', 'abc'))

    def test_rotated_strings(self):
        self.assertTrue(are_Rotations('waterbottle', 'etalebottlewat'))
        self.assertTrue(are_Rotations('practice', 'icepractice'))

    def test_different_lengths(self):
        self.assertFalse(are_Rotations('abc', 'abcd'))
        self.assertFalse(are_Rotations('', 'a'))
        self.assertFalse(are_Rotations('a', ''))

    def test_empty_strings(self):
        self.assertTrue(are_Rotations('', ''))

    def test_single_char_strings(self):
        self.assertTrue(are_Rotations('a', 'a'))
        self.assertFalse(are_Rotations('a', 'b'))

    def test_special_cases(self):
        self.assertTrue(are_Rotations('a', 'A'))
        self.assertTrue(are_Rotations('A', 'a'))
        self.assertFalse(are_Rotations('', 'A'))
        self.assertFalse(are_Rotations('A', ''))
