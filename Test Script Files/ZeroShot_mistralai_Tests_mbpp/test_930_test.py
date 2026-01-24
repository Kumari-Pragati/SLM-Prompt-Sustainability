import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_single_a(self):
        self.assertEqual(text_match('a'), 'Not matched!')

    def test_single_b(self):
        self.assertEqual(text_match('b'), 'Not matched!')

    def test_multiple_a(self):
        self.assertEqual(text_match('aa'), 'Not matched!')

    def test_multiple_ab(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_multiple_abab(self):
        self.assertEqual(text_match('abab'), 'Found a match!')

    def test_multiple_ababab(self):
        self.assertEqual(text_match('ababab'), 'Found a match!')

    def test_multiple_abababab(self):
        self.assertEqual(text_match('abababab'), 'Found a match!')

    def test_multiple_ababababab(self):
        self.assertEqual(text_match('ababababab'), 'Found a match!')

    def test_multiple_abababababab(self):
        self.assertEqual(text_match('abababababab'), 'Found a match!')
