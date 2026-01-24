import unittest
from mbpp_607_code import find_literals

class TestFindLiterals(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 16, 20))

    def test_edge_case_short_pattern(self):
        self.assertEqual(find_literals('a', 'a'), ('a', 0, 1))

    def test_edge_case_long_pattern(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'lazy'), ('lazy', 44, 49))

    def test_edge_case_pattern_not_found(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'zebra'), (None, None, None))

    def test_edge_case_empty_string(self):
        self.assertEqual(find_literals('', 'fox'), (None, None, None))

    def test_edge_case_single_char_string(self):
        self.assertEqual(find_literals('a', 'a'), ('a', 0, 1))
        self.assertEqual(find_literals('A', 'A'), ('A', 0, 1))
