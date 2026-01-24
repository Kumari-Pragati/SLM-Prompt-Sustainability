import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):

    def test_search_literal_found(self):
        pattern = 'test'
        text = 'This is a test string'
        result = search_literal(pattern, text)
        self.assertEqual(result, (10, 14))

    def test_search_literal_not_found(self):
        pattern = 'not_found'
        text = 'This is a test string'
        result = search_literal(pattern, text)
        self.assertIsNone(result)

    def test_search_literal_empty_pattern(self):
        pattern = ''
        text = 'This is a test string'
        result = search_literal(pattern, text)
        self.assertIsNone(result)

    def test_search_literal_empty_text(self):
        pattern = 'test'
        text = ''
        result = search_literal(pattern, text)
        self.assertIsNone(result)
