import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartAEndB(unittest.TestCase):

    def test_match_found(self):
        self.assertEqual(text_starta_endb('acb'), 'Found a match!')
        self.assertEqual(text_starta_endb('abc'), 'Found a match!')
        self.assertEqual(text_starta_endb('abacb'), 'Found a match!')
        self.assertEqual(text_starta_endb('aabbb'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_starta_endb('ab'), 'Not matched!')
        self.assertEqual(text_starta_endb('ba'), 'Not matched!')
        self.assertEqual(text_starta_endb('ac'), 'Not matched!')
        self.assertEqual(text_starta_endb('bc'), 'Not matched!')
        self.assertEqual(text_starta_endb('cab'), 'Not matched!')
        self.assertEqual(text_starta_endb('cba'), 'Not matched!')
        self.assertEqual(text_starta_endb(''), 'Not matched!')
