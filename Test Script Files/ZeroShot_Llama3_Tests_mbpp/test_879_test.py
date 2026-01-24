import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_match(self):
        self.assertEqual(text_match('aabb'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_match_with_capture(self):
        self.assertEqual(text_match('a.*?b'), 'Found a match!')

    def test_no_match_with_capture(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_match_with_capture_group(self):
        self.assertEqual(text_match('a.*?b'), 'Found a match!')

    def test_no_match_with_capture_group(self):
        self.assertEqual(text_match('abc'), 'Not matched!')
