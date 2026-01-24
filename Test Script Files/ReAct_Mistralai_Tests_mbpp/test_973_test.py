import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):

    def test_empty_string(self):
        """Checks that an empty string is rotated correctly."""
        self.assertEqual(left_rotate("", 3), "")

    def test_single_character_string(self):
        """Checks that a single character string is rotated correctly."""
        self.assertEqual(left_rotate("a", 1), "a")
        self.assertEqual(left_rotate("a", 0), "a")
        self.assertEqual(left_rotate("a", 2), "a")

    def test_normal_string(self):
        """Checks that a normal string is rotated correctly."""
        self.assertEqual(left_rotate("abc", 1), "bca")
        self.assertEqual(left_rotate("abc", 2), "cab")
        self.assertEqual(left_rotate("abc", 3), "cba")

    def test_negative_rotation(self):
        """Checks that a negative rotation returns the original string."""
        self.assertEqual(left_rotate("abc", -1), "abc")

    def test_rotation_larger_than_string_length(self):
        """Checks that a rotation larger than the string length wraps around."""
        self.assertEqual(left_rotate("abc", 4), "bca")

    def test_non_integer_rotation(self):
        """Checks that non-integer rotations raise a ValueError."""
        self.assertRaises(ValueError, left_rotate, "abc", 3.5)
