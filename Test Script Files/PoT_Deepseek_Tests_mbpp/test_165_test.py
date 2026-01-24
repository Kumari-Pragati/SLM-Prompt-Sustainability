import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_char_position('ABC'), 3)
        self.assertEqual(count_char_position('abc'), 3)
        self.assertEqual(count_char_position('Abc'), 3)
        self.assertEqual(count_char_position('A1b2c3'), 3)

    def test_edge_cases(self):
        self.assertEqual(count_char_position(''), 0)
        self.assertEqual(count_char_position('A'), 1)
        self.assertEqual(count_char_position('a'), 1)
        self.assertEqual(count_char_position('1'), 0)

    def test_corner_cases(self):
        self.assertEqual(count_char_position('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 26)
        self.assertEqual(count_char_position('abcdefghijklmnopqrstuvwxyz'), 26)
        self.assertEqual(count_char_position('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'), 52)
