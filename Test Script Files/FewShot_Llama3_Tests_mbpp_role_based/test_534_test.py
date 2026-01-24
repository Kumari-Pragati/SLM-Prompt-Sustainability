import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):
    def test_found_pattern(self):
        pattern = "hello"
        text = "hello world"
        result = search_literal(pattern, text)
        self.assertEqual(result, (0, 5))

    def test_pattern_at_end(self):
        pattern = "world"
        text = "hello world"
        result = search_literal(pattern, text)
        self.assertEqual(result, (5, 11))

    def test_pattern_not_found(self):
        pattern = "goodbye"
        text = "hello world"
        result = search_literal(pattern, text)
        self.assertIsNone(result)

    def test_pattern_empty(self):
        pattern = ""
        text = "hello world"
        result = search_literal(pattern, text)
        self.assertIsNone(result)

    def test_text_empty(self):
        pattern = "hello"
        text = ""
        result = search_literal(pattern, text)
        self.assertIsNone(result)
