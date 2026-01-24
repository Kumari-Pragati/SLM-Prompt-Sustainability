import unittest
from mbpp_747_code import lcs_of_three

class TestLCSOfThree(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(lcs_of_three("", "", "", 0, 0, 0), 0)

    def test_single_char_strings(self):
        self.assertEqual(lcs_of_three("a", "", "", 1, 0, 0), 0)
        self.assertEqual(lcs_of_three("", "a", "", 0, 1, 0), 0)
        self.assertEqual(lcs_of_three("", "", "a", 0, 0, 1), 0)
        self.assertEqual(lcs_of_three("a", "a", "", 1, 1, 0), 1)

    def test_identical_strings(self):
        self.assertEqual(lcs_of_three("abc", "abc", "abc", 3, 3, 3), 3)

    def test_different_lengths(self):
        self.assertEqual(lcs_of_three("abc", "abcd", "efg", 3, 4, 3), 2)

    def test_different_strings(self):
        self.assertEqual(lcs_of_three("abc", "def", "ghi", 3, 3, 3), 0)

    def test_longer_string_starts_with_shorter(self):
        self.assertEqual(lcs_of_three("abcdef", "abc", "123", 6, 3, 3), 3)

    def test_longer_string_contains_shorter(self):
        self.assertEqual(lcs_of_three("abcdef", "abc", "xyz", 6, 3, 3), 3)

    def test_longer_string_contains_shorter_twice(self):
        self.assertEqual(lcs_of_three("abcdef", "abc", "lmn", 6, 3, 3), 3)

    def test_error_empty_list(self):
        with self.assertRaises(TypeError):
            lcs_of_three([], [], [], 0, 0, 0)

    def test_error_negative_length(self):
        with self.assertRaises(ValueError):
            lcs_of_three("abc", "abc", "abc", -1, 0, 0)
