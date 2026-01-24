import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):

    def test_typical_case(self):
        pattern = 'hello'
        text = 'hello world'
        self.assertEqual(search_literal(pattern, text), (0, 5))

    def test_edge_case_no_match(self):
        pattern = 'hello'
        text = 'world'
        self.assertIsNone(search_literal(pattern, text))

    def test_edge_case_empty_pattern(self):
        pattern = ''
        text = 'hello world'
        self.assertEqual(search_literal(pattern, text), (0, 0))

    def test_edge_case_empty_text(self):
        pattern = 'hello'
        text = ''
        self.assertIsNone(search_literal(pattern, text))

    def test_edge_case_empty_both(self):
        pattern = ''
        text = ''
        self.assertIsNone(search_literal(pattern, text))

    def test_explicitly_handled_error_case(self):
        pattern = 'hello'
        text = 12345  # Non-string input
        with self.assertRaises(TypeError):
            search_literal(pattern, text)
