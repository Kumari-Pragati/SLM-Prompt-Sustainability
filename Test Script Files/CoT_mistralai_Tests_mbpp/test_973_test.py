import unittest
from973_code import left_rotate

class TestLeftRotate(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(left_rotate("", 3), "")

    def test_single_character_string(self):
        self.assertEqual(left_rotate("a", 2), "a")
        self.assertEqual(left_rotate("a", 1), "a")
        self.assertEqual(left_rotate("a", 0), "a")

    def test_normal_string(self):
        self.assertEqual(left_rotate("abc", 2), "bca")
        self.assertEqual(left_rotate("abc", 1), "bac")

    def test_long_string(self):
        long_string = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(left_rotate(long_string, 10), "ghijklmnopqrstuvwxyzabcdef")

    def test_negative_d(self):
        self.assertRaises(ValueError, left_rotate, "abc", -1)

    def test_d_greater_than_string_length(self):
        self.assertRaises(ValueError, left_rotate, "abc", 13)
