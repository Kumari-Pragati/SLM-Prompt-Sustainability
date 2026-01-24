import unittest
from mbpp_861_code import Counter
from eighty_six_one_code import anagram_lambda

class TestAnagramLambda(unittest.TestCase):

    def test_simple_anagram(self):
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "listen"), ["listen", "silent"])

    def test_case_insensitive_anagram(self):
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "listen".lower()), ["listen", "silent"])

    def test_single_word_anagram(self):
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "s"), [])

    def test_empty_list_anagram(self):
        self.assertListEqual(anagram_lambda([], "listen"), [])

    def test_single_word_input_anagram(self):
        self.assertListEqual(anagram_lambda(["listen"], "listen"), ["listen"])

    def test_no_anagram_case(self):
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "not_anagram"), [])

    def test_anagram_with_special_characters(self):
        self.assertListEqual(anagram_lambda(["listen", "silent", "enlist"], "listen#"), [])
