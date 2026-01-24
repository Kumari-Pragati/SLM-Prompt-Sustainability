import unittest
from708_code import Convert

class TestConvert(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(Convert("word1 word2 word3"), ["word1", "word2", "word3"])

    def test_edge_case_empty_string(self):
        self.assertListEqual(Convert(""), [])

    def test_edge_case_single_word(self):
        self.assertListEqual(Convert("word"), ["word"])

    def test_edge_case_single_space(self):
        self.assertListEqual(Convert(" "), [""])

    def test_edge_case_multiple_spaces(self):
        self.assertListEqual(Convert("word1 word2   word3"), ["word1", "word2", "word3"])

    def test_corner_case_leading_trailing_spaces(self):
        self.assertListEqual(Convert(" word1 word2 word3 "), ["word1", "word2", "word3"])
