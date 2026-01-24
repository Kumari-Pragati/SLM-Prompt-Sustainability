import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):

    def test_are_rotations_same_string(self):
        self.assertTrue(are_Rotations('abc', 'bcab'))
        self.assertTrue(are_Rotations('a', 'a'))
        self.assertTrue(are_Rotations('waterbottle', 'bottlewater'))

    def test_are_not_rotations_different_sizes(self):
        self.assertFalse(are_Rotations('abc', 'abcd'))
        self.assertFalse(are_Rotations('', 'a'))
        self.assertFalse(are_Rotations('abc', 'abcx'))

    def test_are_not_rotations_different_strings(self):
        self.assertFalse(are_Rotations('abc', 'def'))
        self.assertFalse(are_Rotations('123', '456'))
        self.assertFalse(are_Rotations('Hello', 'World'))
