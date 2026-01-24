import unittest
from mbpp_607_code import find_literals

class TestFindLiterals(unittest.TestCase):
    def test_typical_use_case(self):
        pattern = 'fox'
        text = 'The quick brown fox jumps over the lazy dog.'
        self.assertEqual(find_literals(text, pattern), ('fox', 16, 19))

    def test_edge_condition(self):
        pattern = 'fox'
        text = 'fox'
        self.assertEqual(find_literals(text, pattern), ('fox', 0, 3))

    def test_boundary_condition(self):
        pattern = 'fox'
        text = 'fo'
        self.assertIsNone(find_literals(text, pattern))

    def test_invalid_input(self):
        pattern = 123
        text = 'The quick brown fox jumps over the lazy dog.'
        with self.assertRaises(TypeError):
            find_literals(text, pattern)
