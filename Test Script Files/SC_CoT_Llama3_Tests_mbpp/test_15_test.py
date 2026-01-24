import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(split_lowerstring("hello world"), ['hello', 'world'])

    def test_edge_case_start(self):
        self.assertEqual(split_lowerstring("hello"), ['hello'])

    def test_edge_case_end(self):
        self.assertEqual(split_lowerstring("world hello"), ['world', 'hello'])

    def test_edge_case_middle(self):
        self.assertEqual(split_lowerstring("hello world hello"), ['hello', 'world', 'hello'])

    def test_edge_case_no_match(self):
        self.assertEqual(split_lowerstring(""), [])

    def test_edge_case_single_char(self):
        self.assertEqual(split_lowerstring("a"), ['a'])

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(split_lowerstring("hello   world"), ['hello', 'world'])

    def test_edge_case_non_ascii(self):
        self.assertEqual(split_lowerstring("hëllo wörld"), ['hëllo', 'wörld'])

    def test_edge_case_non_ascii_and_spaces(self):
        self.assertEqual(split_lowerstring("hëllo   wörld"), ['hëllo', 'wörld'])

    def test_edge_case_punctuation(self):
        self.assertEqual(split_lowerstring("hello, world!"), ['hello', 'world'])

    def test_edge_case_punctuation_and_spaces(self):
        self.assertEqual(split_lowerstring("hello, world!   "), ['hello', 'world'])

    def test_edge_case_punctuation_and_spaces_and_non_ascii(self):
        self.assertEqual(split_lowerstring("hëllo, wörld!   "), ['hëllo', 'wörld'])
