import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):

    def test_left_rotate_with_empty_string(self):
        self.assertEqual(left_rotate("", 2), "")

    def test_left_rotate_with_single_character(self):
        self.assertEqual(left_rotate("a", 1), "a")

    def test_left_rotate_with_multiple_characters(self):
        self.assertEqual(left_rotate("abc", 1), "bca")
        self.assertEqual(left_rotate("abc", 2), "cab")
        self.assertEqual(left_rotate("abc", 3), "abc")

    def test_left_rotate_with_large_rotation(self):
        self.assertEqual(left_rotate("abc", 4), "bca")

    def test_left_rotate_with_large_string(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(left_rotate(s, 1), "bcdefghijklmnopqrstuvwxyza")
