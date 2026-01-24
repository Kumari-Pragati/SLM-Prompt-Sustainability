import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):

    def test_same_length_strings(self):
        self.assertTrue(are_Rotations('abc', 'cab'))

    def test_strings_of_different_lengths(self):
        self.assertFalse(are_Rotations('abc', 'def'))

    def test_rotated_string(self):
        self.assertTrue(are_Rotations('abc', 'bca'))

    def test_non_rotated_string(self):
        self.assertFalse(are_Rotations('abc', 'def'))

    def test_empty_string(self):
        self.assertFalse(are_Rotations('', ''))

    def test_single_character_string(self):
        self.assertTrue(are_Rotations('a', 'a'))

    def test_single_character_string_non_rotated(self):
        self.assertFalse(are_Rotations('a', 'b'))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            are_Rotations(123, 'abc')

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            are_Rotations('abc', 123)
