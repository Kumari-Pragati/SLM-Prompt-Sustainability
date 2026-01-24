import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):
    def test_found_match(self):
        self.assertEqual(text_match_string('HelloWorld'), 'Found a match!')
        self.assertEqual(text_match_string('12345'), 'Found a match!')
        self.assertEqual(text_match_string('_abcdef'), 'Found a match!')

    def test_not_matched(self):
        self.assertEqual(text_match_string(''), 'Not matched!')
        self.assertEqual(text_match_string(' '), 'Not matched!')
        self.assertEqual(text_match_string('Hello World'), 'Not matched!')
        self.assertEqual(text_match_string('123456'), 'Not matched!')
        self.assertEqual(text_match_string('_abcdefg'), 'Not matched!')

    def test_edge_cases(self):
        self.assertEqual(text_match_string('_'), 'Found a match!')
        self.assertEqual(text_match_string('__'), 'Not matched!')
        self.assertEqual(text_match_string('_123'), 'Found a match!')
        self.assertEqual(text_match_string('123_'), 'Found a match!')
        self.assertEqual(text_match_string('123_456'), 'Not matched!')
