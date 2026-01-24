import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(search_literal('hello', 'hello world hello'), (0, 10))

    def test_edge_case_start(self):
        self.assertEqual(search_literal('hello', 'hello world'), (0, 5))

    def test_edge_case_end(self):
        self.assertEqual(search_literal('world', 'hello world'), (6, 11))

    def test_edge_case_no_match(self):
        self.assertIsNone(search_literal('hello', 'goodbye world'))

    def test_edge_case_empty_pattern(self):
        self.assertIsNone(search_literal('', 'hello world'))

    def test_edge_case_empty_text(self):
        self.assertIsNone(search_literal('hello', ''))

    def test_edge_case_pattern_longer_than_text(self):
        self.assertIsNone(search_literal('hello world', 'hello'))

    def test_edge_case_text_longer_than_pattern(self):
        self.assertEqual(search_literal('hello', 'hello world hello'), (0, 10))

    def test_edge_case_pattern_and_text_empty(self):
        self.assertIsNone(search_literal('', ''))
