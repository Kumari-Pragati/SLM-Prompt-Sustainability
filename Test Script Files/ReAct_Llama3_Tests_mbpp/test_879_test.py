import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_match_found(self):
        self.assertEqual(text_match("a.*?b$"), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match("a.*?c"), 'Not matched!')

    def test_match_found_at_start(self):
        self.assertEqual(text_match("a.*?b$abc"), 'Found a match!')

    def test_match_found_at_end(self):
        self.assertEqual(text_match("abc.*?b$"), 'Found a match!')

    def test_match_found_at_middle(self):
        self.assertEqual(text_match("abc.*?b$def"), 'Found a match!')

    def test_match_not_found_at_start(self):
        self.assertEqual(text_match("c.*?b$"), 'Not matched!')

    def test_match_not_found_at_end(self):
        self.assertEqual(text_match("abc.*?c"), 'Not matched!')

    def test_match_not_found_at_middle(self):
        self.assertEqual(text_match("abc.*?cdef"), 'Not matched!')
