import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):
    def test_valid_rotations(self):
        self.assertTrue(are_Rotations('abc', 'cab'))
        self.assertTrue(are_Rotations('hello', 'lohel'))
        self.assertTrue(are_Rotations('abcabc', 'abcabc'))

    def test_invalid_rotations(self):
        self.assertFalse(are_Rotations('abc', 'def'))
        self.assertFalse(are_Rotations('hello', 'world'))
        self.assertFalse(are_Rotations('abc', 'abcabc'))

    def test_edge_cases(self):
        self.assertTrue(are_Rotations('a', 'a'))
        self.assertFalse(are_Rotations('a', 'b'))
        self.assertFalse(are_Rotations('a', ''))

    def test_empty_strings(self):
        self.assertFalse(are_Rotations('', ''))
        self.assertFalse(are_Rotations('', 'a'))
        self.assertFalse(are_Rotations('a', ''))
