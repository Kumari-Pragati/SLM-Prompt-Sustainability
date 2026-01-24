import unittest
from mbpp_607_code import find_literals

class TestFindLiterals(unittest.TestCase):
    def test_typical_case(self):
        pattern = 'fox'
        text = 'The quick brown fox jumps over the lazy dog.'
        self.assertEqual(find_literals(text, pattern), ('fox', 16, 19))

    def test_edge_case(self):
        pattern = 'fox'
        text = 'fox'
        self.assertEqual(find_literals(text, pattern), ('fox', 0, 3))

    def test_no_match(self):
        pattern = 'fox'
        text = 'The quick brown dog jumps over the lazy cat.'
        self.assertIsNone(find_literals(text, pattern))

    def test_empty_text(self):
        pattern = 'fox'
        text = ''
        self.assertIsNone(find_literals(text, pattern))

    def test_empty_pattern(self):
        pattern = ''
        text = 'The quick brown fox jumps over the lazy dog.'
        self.assertIsNone(find_literals(text, pattern))

    def test_invalid_input(self):
        pattern = 123
        text = 'The quick brown fox jumps over the lazy dog.'
        with self.assertRaises(TypeError):
            find_literals(text, pattern)
