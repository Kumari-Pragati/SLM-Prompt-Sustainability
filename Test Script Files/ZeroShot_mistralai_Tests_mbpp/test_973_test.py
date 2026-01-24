import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(left_rotate("", 2), "")

    def test_single_character_string(self):
        self.assertEqual(left_rotate("a", 2), "a")

    def test_simple_string(self):
        self.assertEqual(left_rotate("abc", 2), "bcab")

    def test_long_string(self):
        self.assertEqual(left_rotate("abcdefghijklmnopqrstuvwxyz", 10), "abcdefghijklmnoqrstuvwxyz")

    def test_negative_shift(self):
        self.assertEqual(left_rotate("abc", -2), "cab")

    def test_shift_greater_than_string_length(self):
        self.assertEqual(left_rotate("abc", 4), "bca")
