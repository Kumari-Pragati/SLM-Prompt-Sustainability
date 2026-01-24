import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):
    def test_match_at_start(self):
        self.assertEqual(text_match_string('hello world'), 'Found a match!')

    def test_match_at_end(self):
        self.assertEqual(text_match_string('world hello'), 'Found a match!')

    def test_match_in_middle(self):
        self.assertEqual(text_match_string('hello world hello'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            text_match_string(123)
