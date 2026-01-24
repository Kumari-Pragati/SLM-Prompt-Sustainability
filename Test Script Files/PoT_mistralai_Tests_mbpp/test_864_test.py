import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):
    def test_typical_cases(self):
        self.assertListEqual(palindrome_lambda(["racecar", "level", "madam"]), ["racecar", "level"])
        self.assertListEqual(palindrome_lambda(["hello", "world", "madam", "racecar"]), [])

    def test_edge_cases(self):
        self.assertListEqual(palindrome_lambda([""]), [])
        self.assertListEqual(palindrome_lambda(["a"]), [])
        self.assertListEqual(palindrome_lambda(["aa"]), ["aa"])
        self.assertListEqual(palindrome_lambda(["abba"]), ["abba"])
        self.assertListEqual(palindrome_lambda(["A", "B", "A"]), [])

    def test_boundary_cases(self):
        self.assertListEqual(palindrome_lambda([" ", " ", " "]), [])
        self.assertListEqual(palindrome_lambda(["\n", "\n", "\n"]), [])
        self.assertListEqual(palindrome_lambda(["\t", "\t", "\t"]), [])
        self.assertListEqual(palindrome_lambda(["!", ".", "?"]), [])
        self.assertListEqual(palindrome_lambda(["!", ".", "!"]), [])
