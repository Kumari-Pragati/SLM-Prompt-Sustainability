import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):
    def test_rotations_of_same_string(self):
        self.assertTrue(are_Rotations('abc', 'bca'))

    def test_rotations_of_different_strings(self):
        self.assertFalse(are_Rotations('abc', 'def'))

    def test_empty_string(self):
        self.assertFalse(are_Rotations('', ''))

    def test_single_character_strings(self):
        self.assertTrue(are_Rotations('a', 'a'))
        self.assertFalse(are_Rotations('a', 'b'))

    def test_strings_of_different_lengths(self):
        self.assertFalse(are_Rotations('abc', 'abcd'))

    def test_strings_with_spaces(self):
        self.assertFalse(are_Rotations('abc def', 'def abc'))
