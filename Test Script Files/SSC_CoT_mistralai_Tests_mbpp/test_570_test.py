import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_normal_case(self):
        self.assertListEqual(remove_words(["hello world", "goodbye universe"], ["o", "d"]), ["hello", "world", "goodbye", "universe"])

    def test_edge_case_empty_list(self):
        self.assertListEqual(remove_words([], ["a", "b"]), [])

    def test_edge_case_empty_charlist(self):
        self.assertListEqual(remove_words(["a", "b", "c"], []), ["a", "b", "c"])

    def test_edge_case_single_word(self):
        self.assertListEqual(remove_words(["word"], ["o"]), ["word"])

    def test_edge_case_single_char_in_word(self):
        self.assertListEqual(remove_words(["wordo", "world"], ["o"]), ["world"])

    def test_edge_case_multiple_chars_in_word(self):
        self.assertListEqual(remove_words(["wordo", "world"], ["o", "d"]), [])

    def test_edge_case_whitespace_only(self):
        self.assertListEqual(remove_words([" ", "\t", "\n"], ["o", "d"]), [])
