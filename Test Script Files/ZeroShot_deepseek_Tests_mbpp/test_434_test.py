import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):

    def test_match_one(self):
        self.assertEqual(text_match_one('ab'), 'Found a match!')
        self.assertEqual(text_match_one('a'), 'Not matched!')
        self.assertEqual(text_match_one('abb'), 'Found a match!')
        self.assertEqual(text_match_one('abbb'), 'Found a match!')
        self.assertEqual(text_match_one('abbbbb'), 'Found a match!')
        self.assertEqual(text_match_one('ac'), 'Not matched!')
