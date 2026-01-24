import unittest
from mbpp_861_code import Counter
from your_module import anagram_lambda  # replace 'your_module' with the actual module name

class TestAnagramLambda(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(anagram_lambda([], "abc"), [])

    def test_single_element(self):
        self.assertListEqual(anagram_lambda(["abc"], "abc"), ["abc"])
        self.assertListEqual(anagram_lambda(["abc"], "def"), [])

    def test_multiple_elements(self):
        self.assertListEqual(anagram_lambda(["abc", "cba", "def"], "abc"), ["abc", "cba"])
        self.assertListEqual(anagram_lambda(["abc", "cba", "def"], "def"), ["def"])
        self.assertListEqual(anagram_lambda(["abc", "cba", "def"], "cba"), ["abc", "cba"])
