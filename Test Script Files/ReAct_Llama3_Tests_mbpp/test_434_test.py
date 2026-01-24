import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):

    def test_match(self):
        self.assertEqual(text_match_one('ab'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_one('abc'), 'Not matched!')

    def test_match_with_plus(self):
        self.assertEqual(text_match_one('abbb'), 'Found a match!')

    def test_no_match_with_plus(self):
        self.assertEqual(text_match_one('abcde'), 'Not matched!')

    def test_match_with_question_mark(self):
        self.assertEqual(text_match_one('ab?'), 'Found a match!')

    def test_no_match_with_question_mark(self):
        self.assertEqual(text_match_one('abc'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_one(''), 'Not matched!')

    def test_none_input(self):
        with self.assertRaises(TypeError):
            text_match_one(None)
