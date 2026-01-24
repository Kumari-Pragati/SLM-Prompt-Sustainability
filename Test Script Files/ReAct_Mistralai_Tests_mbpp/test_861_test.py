import unittest
from mbpp_861_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(anagram_lambda([], "abc"), [])

    def test_single_element(self):
        self.assertListEqual(anagram_lambda(["abc"], "abc"), ["abc"])
        self.assertListEqual(anagram_lambda(["abc"], "abcd"), [])

    def test_multiple_elements(self):
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "listen"), ["listen", "enlist"])
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "silent"), ["listen", "enlist"])
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "enlist"), ["listen", "silent"])
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "enlis"), [])

    def test_case_sensitivity(self):
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "LISTEN"), [])
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "listEN"), [])
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "listeN"), [])

    def test_empty_string(self):
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], ""), [])

    def test_single_char_string(self):
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "a"), [])
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "b"), [])
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "c"), [])
