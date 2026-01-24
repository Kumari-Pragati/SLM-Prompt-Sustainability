import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match_string('hello'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_edge_case(self):
        self.assertEqual(text_match_string('123'), 'Not matched!')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            text_match_string(123)

    def test_empty_string_input(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_non_ascii_input(self):
        self.assertEqual(text_match_string('hello world'), 'Found a match!')

    def test_multiple_spaces_input(self):
        self.assertEqual(text_match_string('hello   world'), 'Found a match!')
