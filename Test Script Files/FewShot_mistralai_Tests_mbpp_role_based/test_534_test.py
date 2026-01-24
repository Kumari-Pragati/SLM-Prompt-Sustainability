import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(search_literal(r'abc', 'abcdefgabc'), (2, 4))

    def test_match_not_found(self):
        self.assertEqual(search_literal(r'xyz', 'abcdefg'), None)

    def test_empty_text(self):
        self.assertEqual(search_literal(r'abc', ''), None)

    def test_pattern_not_string(self):
        with self.assertRaises(TypeError):
            search_literal(123, 'abc')

    def test_pattern_empty(self):
        with self.assertRaises(ValueError):
            search_literal('', 'abc')
