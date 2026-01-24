import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(search_literal('hello', 'hello world'), (0, 5))

    def test_no_match(self):
        self.assertIsNone(search_literal('hello', 'goodbye world'))

    def test_match_at_start(self):
        self.assertEqual(search_literal('world', 'hello world'), (6, 11))

    def test_match_at_end(self):
        self.assertEqual(search_literal('world', 'hello world world'), (9, 15))

    def test_match_at_middle(self):
        self.assertEqual(search_literal('or', 'hello world or goodbye'), (7, 11))

    def test_empty_pattern(self):
        self.assertIsNone(search_literal('', 'hello world'))

    def test_empty_text(self):
        self.assertIsNone(search_literal('hello', ''))

    def test_pattern_longer_than_text(self):
        self.assertIsNone(search_literal('hello world', 'hello'))

    def test_text_longer_than_pattern(self):
        self.assertEqual(search_literal('hello', 'hello world world'), (0, 5))
