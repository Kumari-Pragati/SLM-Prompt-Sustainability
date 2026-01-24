import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(text_match('hello_world'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match('hello'), 'Not matched!')

    def test_match_found_at_start(self):
        self.assertEqual(text_match('hello_world123'), 'Found a match!')

    def test_match_found_at_end(self):
        self.assertEqual(text_match('hello123_world'), 'Found a match!')

    def test_match_found_in_middle(self):
        self.assertEqual(text_match('hello123_world456'), 'Found a match!')

    def test_match_not_found_at_start(self):
        self.assertEqual(text_match('123hello_world'), 'Not matched!')

    def test_match_not_found_at_end(self):
        self.assertEqual(text_match('hello_world456'), 'Not matched!')

    def test_match_not_found_in_middle(self):
        self.assertEqual(text_match('hello123_world456'), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match(123)
