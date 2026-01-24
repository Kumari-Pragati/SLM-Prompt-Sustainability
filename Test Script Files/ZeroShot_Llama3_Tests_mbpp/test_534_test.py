import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):

    def test_search_literal_found(self):
        result = search_literal('hello', 'hello world hello')
        self.assertEqual(result, (6, 11))

    def test_search_literal_not_found(self):
        result = search_literal('hello', 'goodbye world')
        self.assertIsNone(result)

    def test_search_literal_empty_text(self):
        result = search_literal('hello', '')
        self.assertIsNone(result)

    def test_search_literal_empty_pattern(self):
        result = search_literal('', 'hello world')
        self.assertIsNone(result)

    def test_search_literal_found_at_start(self):
        result = search_literal('world', 'world hello world')
        self.assertEqual(result, (0, 5))

    def test_search_literal_found_at_end(self):
        result = search_literal('world', 'hello world world')
        self.assertEqual(result, (7, 12))

    def test_search_literal_found_multiple_times(self):
        result = search_literal('o', 'hello world hello')
        self.assertEqual(result, (4, 5))
