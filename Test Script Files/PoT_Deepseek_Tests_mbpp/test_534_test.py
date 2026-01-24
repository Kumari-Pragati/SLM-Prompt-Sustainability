import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(search_literal('a', 'abc'), (0, 1))

    def test_edge_case_no_match(self):
        self.assertIsNone(search_literal('z', 'abc'))

    def test_boundary_case_empty_string(self):
        self.assertIsNone(search_literal('a', ''))

    def test_boundary_case_pattern_empty_string(self):
        self.assertIsNone(search_literal('', 'abc'))

    def test_corner_case_pattern_at_end(self):
        self.assertEqual(search_literal('c', 'abc'), (2, 3))

    def test_corner_case_pattern_at_start(self):
        self.assertEqual(search_literal('a', 'abc'), (0, 1))

    def test_corner_case_multiple_matches(self):
        self.assertEqual(search_literal('b', 'abba'), (1, 2))
