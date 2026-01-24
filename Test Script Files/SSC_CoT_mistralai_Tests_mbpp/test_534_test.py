import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(search_literal('abc', 'abcdabc'), (1, 3))
        self.assertEqual(search_literal('xyz', 'xyzabc'), (2, 4))

    def test_edge_cases(self):
        self.assertEqual(search_literal('abc', 'ab'), (0, 2))
        self.assertEqual(search_literal('abc', 'abcdefg'), (4, 6))
        self.assertEqual(search_literal('abc', 'abcabc'), (0, 3))
        self.assertEqual(search_literal('abc', 'abcabcabc'), (0, 3))

    def test_boundary_cases(self):
        self.assertEqual(search_literal('abc', 'a'), (0, 1))
        self.assertEqual(search_literal('abc', 'abc'), (0, 3))
        self.assertEqual(search_literal('abc', 'abcdef'), (0, 3))
        self.assertEqual(search_literal('abc', 'abcdefg'), (0, 3))
        self.assertEqual(search_literal('abc', 'abcdefgh'), (0, 3))

    def test_empty_string(self):
        self.assertEqual(search_literal('abc', ''), (None, None))

    def test_no_match(self):
        self.assertEqual(search_literal('abc', 'def'), (None, None))
