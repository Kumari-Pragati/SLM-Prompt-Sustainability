import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):

    def test_equal_strings(self):
        self.assertTrue(are_Rotations('abc', 'abc'))

    def test_rotated_strings(self):
        self.assertTrue(are_Rotations('abc', 'cab'))

    def test_non_rotated_strings(self):
        self.assertFalse(are_Rotations('abc', 'def'))

    def test_strings_of_different_lengths(self):
        self.assertFalse(are_Rotations('abc', 'defgh'))

    def test_empty_string(self):
        self.assertTrue(are_Rotations('', ''))

    def test_single_character_string(self):
        self.assertTrue(are_Rotations('a', 'a'))

    def test_rotated_string_with_spaces(self):
        self.assertTrue(are_Rotations('hello world', 'world hello'))

    def test_non_rotated_string_with_spaces(self):
        self.assertFalse(are_Rotations('hello world', 'goodbye moon'))
