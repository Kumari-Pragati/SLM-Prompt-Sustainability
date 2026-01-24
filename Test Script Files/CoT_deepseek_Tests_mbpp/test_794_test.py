import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartAEndB(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_starta_endb('acb'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_starta_endb('abc'), 'Not matched!')

    def test_multiple_a_and_b(self):
        self.assertEqual(text_starta_endb('aacb'), 'Found a match!')

    def test_a_only(self):
        self.assertEqual(text_starta_endb('a'), 'Not matched!')

    def test_b_only(self):
        self.assertEqual(text_starta_endb('b'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_starta_endb(''), 'Not matched!')

    def test_special_characters(self):
        self.assertEqual(text_starta_endb('@acb@'), 'Found a match!')

    def test_numbers(self):
        self.assertEqual(text_starta_endb('123acb456'), 'Found a match!')

    def test_whitespace(self):
        self.assertEqual(text_starta_endb('acb '), 'Found a match!')
