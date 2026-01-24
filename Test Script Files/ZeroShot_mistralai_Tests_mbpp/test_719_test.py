import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_single_a(self):
        self.assertEqual(text_match('a'), 'Not matched!')

    def test_single_b(self):
        self.assertEqual(text_match('b'), 'Not matched!')

    def test_single_ab(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_multiple_a(self):
        self.assertEqual(text_match('aaaaa'), 'Found a match!')

    def test_multiple_ab(self):
        self.assertEqual(text_match('ababab'), 'Found a match!')

    def test_multiple_b_at_start(self):
        self.assertEqual(text_match('bbab'), 'Found a match!')

    def test_multiple_b_at_end(self):
        self.assertEqual(text_match('abbb'), 'Found a match!')

    def test_multiple_b_in_middle(self):
        self.assertEqual(text_match('abbbab'), 'Found a match!')
