import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(search_literal('a', 'abc'), (1, 2))

    def test_no_match(self):
        self.assertIsNone(search_literal('a', 'bcd'))

    def test_empty_pattern(self):
        self.assertIsNone(search_literal('', 'abc'))

    def test_empty_text(self):
        self.assertIsNone(search_literal('a', ''))

    def test_empty_both(self):
        self.assertIsNone(search_literal('', ''))

    def test_start_of_text(self):
        self.assertEqual(search_literal('abc', 'abcdef'), (0, 3))

    def test_end_of_text(self):
        self.assertEqual(search_literal('xyz', 'abcdefxyz'), (6, 9))

    def test_complex_match(self):
        self.assertEqual(search_literal('def', 'abcdefghi'), (3, 6))
