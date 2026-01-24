import unittest
from mbpp_338_code import count_Substring_With_Equal_Ends

class TestCountSubstring(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_palindrome(self):
        self.assertEqual(count_Substring_With_Equal_Ends("racecar"), 6)

    def test_non_palindrome(self):
        self.assertEqual(count_Substring_With_Equal_Ends("hello"), 1)

    def test_mixed_case(self):
        self.assertEqual(count_Substring_With_Equal_Ends("HeLLo"), 1)

    def test_special_characters(self):
        self.assertEqual(count_Substring_With_Equal_Ends("!@#$%^&*()_"), 0)

    def test_multiple_palindromes(self):
        self.assertEqual(count_Substring_With_Equal_Ends("racecarabbacaddcar"), 11)
