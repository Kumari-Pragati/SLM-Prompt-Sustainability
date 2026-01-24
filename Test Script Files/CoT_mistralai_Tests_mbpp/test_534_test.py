import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):
    def test_empty_pattern(self):
        self.assertIsNone(search_literal('', 'test'))

    def test_empty_text(self):
        self.assertIsNone(search_literal('abc', ''))

    def test_single_match(self):
        self.assertEqual(search_literal('abc', 'abcdefg'), (0, 3))

    def test_multiple_matches(self):
        self.assertEqual(search_literal('ab', 'abcabc'), (0, 2))
        self.assertEqual(search_literal('ab', 'abcabcd'), (0, 2))
        self.assertEqual(search_literal('ab', 'abcabcabc'), (0, 2))

    def test_no_match(self):
        self.assertIsNone(search_literal('xyz', 'abcdefg'))

    def test_case_insensitive(self):
        self.assertEqual(search_literal('ABC', 'abcdefgABC', re.IGNORECASE), (6, 9))

    def test_start_at_end(self):
        self.assertEqual(search_literal('abc', 'abc'), (3, 6))

    def test_end_at_start(self):
        self.assertEqual(search_literal('abc', 'abc'), (0, 3))

    def test_match_at_boundary(self):
        self.assertEqual(search_literal('ab', 'aab'), (0, 2))
        self.assertEqual(search_literal('ab', 'aba'), (1, 3))

    def test_match_with_whitespace(self):
        self.assertEqual(search_literal('abc', ' abc def abc '), (2, 5))

    def test_invalid_input(self):
        self.assertRaises(TypeError, search_literal, 123, 'abc')
        self.assertRaises(TypeError, search_literal, 'abc', 123)
