import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(search_literal('abc', 'abcdefg'), (0, 3))

    def test_match_at_end(self):
        self.assertEqual(search_literal('abc', 'defgabc'), (6, 9))

    def test_match_in_middle(self):
        self.assertEqual(search_literal('xyz', 'abcxyzdef'), (3, 8))

    def test_empty_text(self):
        self.assertEqual(search_literal('abc', ''), None)

    def test_empty_pattern(self):
        self.assertEqual(search_literal('', 'abcdefg'), None)

    def test_no_match(self):
        self.assertEqual(search_literal('xyz', 'abcdefg'), None)

    def test_match_with_flags(self):
        self.assertEqual(search_literal('(abc)', '(abcdefg)', re.FULL), (0, 3))
