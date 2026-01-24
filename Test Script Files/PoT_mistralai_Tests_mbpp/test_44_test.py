import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_match_string('HelloWorld'), 'Found a match!')
        self.assertEqual(text_match_string('12345'), 'Found a match!')
        self.assertEqual(text_match_string('_abcdef'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match_string(''), 'Not matched!')
        self.assertEqual(text_match_string(' '), 'Not matched!')
        self.assertEqual(text_match_string('_'), 'Not matched!')
        self.assertEqual(text_match_string('__'), 'Not matched!')

    def test_corner_case(self):
        self.assertEqual(text_match_string('_123'), 'Found a match!')
        self.assertEqual(text_match_string('123_'), 'Found a match!')
        self.assertEqual(text_match_string('123_45'), 'Found a match!')
        self.assertEqual(text_match_string('_456'), 'Not matched!')
