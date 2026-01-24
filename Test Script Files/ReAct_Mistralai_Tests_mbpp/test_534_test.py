import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):

    def test_empty_pattern(self):
        with self.assertRaises(ValueError):
            search_literal('', 'some text')

    def test_empty_text(self):
        with self.assertRaises(ValueError):
            search_literal('abc', '')

    def test_no_match(self):
        self.assertIsNone(search_literal('def', 'abc'))

    def test_single_match(self):
        self.assertEqual(search_literal('abc', 'abcdefg'), (0, 3))

    def test_multiple_matches(self):
        self.assertEqual(search_literal('ab', 'ababab'), (0, 2))
        self.assertEqual(search_literal('ab', 'abababcdab'), (0, 2))
        self.assertEqual(search_literal('ab', 'abababcdabefgab'), (0, 2))

    def test_match_at_end(self):
        self.assertEqual(search_literal('abc', 'xyzabc'), (7, 10))

    def test_match_at_beginning(self):
        self.assertEqual(search_literal('abc', 'abcxyz'), (0, 3))

    def test_match_with_whitespace(self):
        self.assertEqual(search_literal('\\s+', '   foo   '), (0, 3))

    def test_match_with_special_characters(self):
        self.assertEqual(search_literal('\\w+', '123Foo_Bar456'), (1, 5))
        self.assertEqual(search_literal('\\d+', '123Foo_Bar456'), (0, 3))
        self.assertEqual(search_literal('\\D+', '123Foo_Bar456'), (4, 10))
