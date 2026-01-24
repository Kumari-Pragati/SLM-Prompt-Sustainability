import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(text_match_word('HelloWorld'), 'Found a match!')

    def test_edge_condition(self):
        self.assertEqual(text_match_word(''), 'Not matched!')

    def test_boundary_condition(self):
        self.assertEqual(text_match_word('HelloWorld1234567890'), 'Found a match!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match_word(12345)
