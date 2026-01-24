import unittest
from mbpp_319_code import findall

class TestFindLongWord(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(find_long_word("This is a long word in this sentence"), ["long"])
        self.assertListEqual(find_long_word("The quick brown fox jumps over the lazy dog"), ["brown", "fox"])

    def test_edge_cases(self):
        self.assertListEqual(find_long_word("a"), [])
        self.assertListEqual(find_long_word("a word"), ["word"])
        self.assertListEqual(find_long_word("a very long word"), ["long"])
        self.assertListEqual(find_long_word("a very long word with numbers 12345"), ["long"])

    def test_special_cases(self):
        self.assertListEqual(find_long_word("The quick brown fox jumps over the lazy dog's tail"), ["brown", "fox"])
        self.assertListEqual(find_long_word("The quick brown fox jumps over the lazy dog's tail, and the cat sat on the mat"), ["brown", "fox"])
        self.assertListEqual(find_long_word("The quick brown fox jumps over the lazy dog's tail, and the cat sat on the mat, and the elephant danced"), ["brown", "fox"])

    def test_invalid_inputs(self):
        self.assertListEqual(find_long_word(123), [])
        self.assertListEqual(find_long_word(None), [])
        self.assertListEqual(find_long_word(""), [])
        self.assertListEqual(find_long_word(" "), [])
