import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):

    def test_found(self):
        self.assertEqual(search_literal('hello', 'hello world hello'), (0, 11))

    def test_not_found(self):
        self.assertIsNone(search_literal('hello', 'goodbye world'))

    def test_multiple_matches(self):
        self.assertEqual(search_literal('hello|world', 'hello world hello'), (0, 5))

    def test_empty_pattern(self):
        self.assertIsNone(search_literal('', 'hello world'))

    def test_empty_text(self):
        self.assertIsNone(search_literal('hello', ''))

    def test_pattern_longer_than_text(self):
        self.assertIsNone(search_literal('hello world', 'hello'))

    def test_text_longer_than_pattern(self):
        self.assertEqual(search_literal('hello', 'hello world hello'), (0, 11))

    def test_pattern_with_special_chars(self):
        self.assertEqual(search_literal('hello.*world', 'hello world hello'), (0, 11))

    def test_text_with_special_chars(self):
        self.assertEqual(search_literal('hello.*world', 'hello world hello.*world'), (0, 11))
