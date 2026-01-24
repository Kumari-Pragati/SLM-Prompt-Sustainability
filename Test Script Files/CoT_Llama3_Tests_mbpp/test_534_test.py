import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):
    def test_found_pattern(self):
        self.assertEqual(search_literal('hello', 'hello world hello'), (0, 10))

    def test_not_found_pattern(self):
        self.assertIsNone(search_literal('hello', 'goodbye world'))

    def test_pattern_at_start(self):
        self.assertEqual(search_literal('world', 'world hello'), (0, 5))

    def test_pattern_at_end(self):
        self.assertEqual(search_literal('hello', 'hello world'), (0, 5))

    def test_pattern_multiple_occurrences(self):
        self.assertEqual(search_literal('hello', 'hello world hello again'), (0, 5))

    def test_pattern_empty(self):
        self.assertIsNone(search_literal('', 'hello world'))

    def test_pattern_none(self):
        self.assertIsNone(search_literal(None, 'hello world'))

    def test_text_empty(self):
        self.assertIsNone(search_literal('hello', ''))

    def test_text_none(self):
        self.assertIsNone(search_literal('hello', None))
