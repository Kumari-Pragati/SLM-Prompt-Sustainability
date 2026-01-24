import unittest
from mbpp_747_code import lcs_of_three

class TestLCSofThree(unittest.TestCase):

    def test_lcs_of_three(self):
        self.assertEqual(lcs_of_three("abc", "def", "ghi", 3, 3, 3), 0)
        self.assertEqual(lcs_of_three("abc", "def", "abc", 3, 3, 3), 3)
        self.assertEqual(lcs_of_three("abc", "def", "def", 3, 3, 3), 3)
        self.assertEqual(lcs_of_three("abc", "def", "abcde", 3, 4, 5), 3)
        self.assertEqual(lcs_of_three("abc", "def", "defgh", 3, 4, 5), 3)
        self.assertEqual(lcs_of_three("abc", "def", "abcdeh", 3, 4, 5), 3)
        self.assertEqual(lcs_of_three("abc", "def", "defghij", 3, 4, 6), 3)
        self.assertEqual(lcs_of_three("abc", "def", "abcdehij", 3, 4, 6), 3)
        self.assertEqual(lcs_of_three("abc", "def", "defghijkl", 3, 4, 6), 3)
        self.assertEqual(lcs_of_three("abc", "def", "abcdehijkl", 3, 4, 6), 3)
        self.assertEqual(lcs_of_three("abc", "def", "defghijklm", 3, 4, 6), 3)
        self.assertEqual(lcs_of_three("abc", "def", "abcdehijklmn", 3, 4, 7), 3)
        self.assertEqual(lcs_of_three("abc", "def", "defghijklmnop", 3, 4, 8), 3)
        self.assertEqual(lcs_of_three("abc", "def", "abcdehijklmnopq", 3, 4, 9), 3)
        self.assertEqual(lcs_of_three("abc", "def", "defghijklmnopqrstu", 3, 4, 10), 3)
        self.assertEqual(lcs_of_three("abc", "def", "abcdehijklmnopqrstuv", 3, 4, 11), 3)
        self.assertEqual(lcs_of_three("abc", "def", "defghijklmnopqrstuvwxy", 3, 4, 12), 3)
        self.assertEqual(lcs_of_three("abc", "def", "abcdehijklmnopqrstuvwxyz", 3, 4, 13), 3)
        self.assertEqual(lcs_of_three("abc", "def", "defghijklmnopqrstuvwxyyz", 3, 4, 14), 3)
        self.assertEqual(lcs_of_three("abc", "def", "abcdehijklmnopqrstuvwxyyz", 3, 4, 15), 3)
        self.assertEqual(lcs_of_three("abc", "def", "defghijklmnopqrstuvwxyyz", 3, 4, 16), 3)
        self.assertEqual(lcs_of_three("abc", "def", "abcdehijklmnopqrstuvwxyyz", 3, 4, 17), 3)
        self.assertEqual(lcs_of_three("abc", "def", "defghijklmnopqrstuvwxyyz", 3, 4, 18), 3)
        self.assertEqual(lcs_of_three("abc", "def", "abcdehijklmnopqrstuvwxyyz", 3, 4, 19), 3)
        self.assertEqual(lcs_of_three("abc", "def", "defghijklmnopqrstuvwxyyz", 3, 4, 20), 3)
        self.assertEqual(lcs_of_three("abc", "def", "abcdehijklmnopqrstuvwxyyz", 3, 4, 21), 3)
        self.assertEqual(lcs_of_three("abc", "def", "defghijklmnopqrstuvwxyyz", 3, 4, 22), 3)
        self.assertEqual(lcs_of_three("abc", "def", "abcdehijklmnopqrstuvwxyyz", 3, 4, 23), 3)
        self.assertEqual(lcs_of_three("abc", "def", "defghijklmnopqrstuvwxyyz", 3, 4, 24), 3)
        self.assertEqual(lcs_of_three("abc", "def", "abcdehijklmnopqrstuvwxyyz", 3, 4, 25), 3)
        self.assertEqual(lcs_of