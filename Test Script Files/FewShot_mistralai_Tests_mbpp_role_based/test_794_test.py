import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartaEndb(unittest.TestCase):
    def test_found_match(self):
        self.assertEqual(text_starta_endb('aaab'), 'Found a match!')
        self.assertEqual(text_starta_endb('abcda'), 'Found a match!')
        self.assertEqual(text_starta_endb('aabbbc'), 'Found a match!')

    def test_not_found_match(self):
        self.assertEqual(text_starta_endb('abcd'), 'Not matched!')
        self.assertEqual(text_starta_endb('a'), 'Not matched!')
        self.assertEqual(text_starta_endb('aaabbb'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_starta_endb(''), 'Not matched!')

    def test_no_a_or_b(self):
        self.assertEqual(text_starta_endb('ccc'), 'Not matched!')
        self.assertEqual(text_starta_endb('bbb'), 'Not matched!')
