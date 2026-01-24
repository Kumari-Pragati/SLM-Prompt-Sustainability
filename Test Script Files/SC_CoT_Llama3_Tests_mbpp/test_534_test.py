import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):
    def test_found(self):
        self.assertEqual(search_literal('abc', 'abcde'), (0, 3))

    def test_not_found(self):
        self.assertIsNone(search_literal('abc', 'defgh'))

    def test_found_at_start(self):
        self.assertEqual(search_literal('abc', 'abcdef'), (0, 3))

    def test_found_at_end(self):
        self.assertEqual(search_literal('abc', 'defabc'), (3, 6))

    def test_found_multiple_times(self):
        self.assertEqual(search_literal('ab', 'ababab'), (0, 2))

    def test_found_at_start_multiple_times(self):
        self.assertEqual(search_literal('ab', 'abababab'), (0, 2))

    def test_found_at_end_multiple_times(self):
        self.assertEqual(search_literal('ab', 'ababababab'), (6, 8))

    def test_empty_pattern(self):
        self.assertIsNone(search_literal('', 'abcde'))

    def test_empty_text(self):
        self.assertIsNone(search_literal('abc', ''))

    def test_pattern_longer_than_text(self):
        self.assertIsNone(search_literal('abcdef', 'abc'))

    def test_text_longer_than_pattern(self):
        self.assertEqual(search_literal('abc', 'abcdef'), (0, 3))

    def test_pattern_and_text_empty(self):
        self.assertIsNone(search_literal('', ''))
