import unittest
from mbpp_861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):
    def test_anagram_with_two_strings(self):
        self.assertListEqual(anagram_lambda(["listen", "silent"], "listen"), ["listen", "silent"])

    def test_anagram_with_one_string(self):
        self.assertListEqual(anagram_lambda(["listen"], "listen"), ["listen"])

    def test_anagram_with_empty_list(self):
        self.assertListEqual(anagram_lambda([], "listen"), [])

    def test_anagram_with_different_lengths(self):
        self.assertListEqual(anagram_lambda(["listen", "silent", "noise"], "listen"), ["listen"])

    def test_anagram_with_case_sensitivity(self):
        self.assertListEqual(anagram_lambda(["Listen", "silent"], "listen"), ["Listen"])

    def test_anagram_with_no_anagrams(self):
        self.assertListEqual(anagram_lambda(["listen", "silent", "noise"], "apple"), [])

    def test_anagram_with_empty_string(self):
        self.assertListEqual(anagram_lambda(["listen", "silent", "noise"], ""), [])
