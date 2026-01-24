import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match('hello_world'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match('hello'), 'Not matched!')

    def test_edge_case(self):
        self.assertEqual(text_match('hello_world123'), 'Not matched!')

    def test_empty_input(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            text_match(123)

    def test_invalid_pattern(self):
        patterns = '^[a-zA-Z]+$'
        self.assertEqual(text_match('hello_world'), 'Not matched!')
