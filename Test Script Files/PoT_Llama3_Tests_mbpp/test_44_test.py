import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(text_match_string('hello'), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match_string('123'), 'Not matched!')

    def test_edge_match(self):
        self.assertEqual(text_match_string('Hello'), 'Found a match!')

    def test_edge_no_match(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_corner_match(self):
        self.assertEqual(text_match_string('a'), 'Found a match!')

    def test_corner_no_match(self):
        self.assertEqual(text_match_string(''), 'Not matched!')
