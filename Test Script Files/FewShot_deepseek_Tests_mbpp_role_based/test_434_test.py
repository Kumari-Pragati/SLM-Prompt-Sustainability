import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_match_one('ab'), 'Found a match!')
        self.assertEqual(text_match_one('abb'), 'Found a match!')
        self.assertEqual(text_match_one('abbb'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match_one('a'), 'Not matched!')
        self.assertEqual(text_match_one(''), 'Not matched!')

    def test_boundary_case(self):
        self.assertEqual(text_match_one('ab?'), 'Found a match!')
        self.assertEqual(text_match_one('ab??'), 'Found a match!')
        self.assertEqual(text_match_one('ab???'), 'Found a match!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match_one(123)
