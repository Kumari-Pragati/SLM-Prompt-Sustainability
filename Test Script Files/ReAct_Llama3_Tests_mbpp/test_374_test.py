import unittest
from mbpp_374_code import permute_string

class TestPermuteString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(permute_string(""), [''])

    def test_single_character_string(self):
        self.assertEqual(permute_string("a"), ["a"])

    def test_two_character_string(self):
        self.assertEqual(permute_string("ab"), ["a", "b", "ab"])

    def test_three_character_string(self):
        self.assertEqual(permute_string("abc"), ["a", "b", "c", "ab", "ac", "bc", "abc"])

    def test_four_character_string(self):
        self.assertEqual(permute_string("abcd"), ["a", "b", "c", "d", "ab", "ac", "ad", "bc", "bd", "cd", "abcd"])

    def test_five_character_string(self):
        self.assertEqual(permute_string("abcde"), ["a", "b", "c", "d", "e", "ab", "ac", "ad", "ae", "bc", "bd", "be", "cd", "ce", "de", "abc", "abd", "abe", "bce", "bde", "cde", "abcde"])

    def test_string_with_duplicates(self):
        self.assertEqual(permute_string("aabb"), ["a", "b", "aa", "ab", "ba", "bb", "aabb"])

    def test_string_with_duplicates_and_trailing_zeros(self):
        self.assertEqual(permute_string("aabbcc"), ["a", "b", "c", "aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc", "aabb", "aabc", "abbc", "abcc", "bacc", "bbcc", "aabbcc"])
