import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):
    def test_left_rotate_positive_numbers(self):
        self.assertEqual(left_rotate("abc", 1), "bca")
        self.assertEqual(left_rotate("abcdefg", 3), "cdefgaba")

    def test_left_rotate_zero(self):
        self.assertEqual(left_rotate("", 0), "")
        self.assertEqual(left_rotate("abc", 0), "abc")

    def test_left_rotate_negative_index(self):
        self.assertEqual(left_rotate("abc", -1), "bca")
        self.assertEqual(left_rotate("abc", -3), "cab")

    def test_left_rotate_empty_string_and_negative_index(self):
        self.assertEqual(left_rotate("", -1), "")

    def test_left_rotate_string_with_only_one_character(self):
        self.assertEqual(left_rotate("a", 1), "b")
        self.assertEqual(left_rotate("a", -1), "b")
