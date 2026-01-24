import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_max_occuring_char('aabbbcc'), 'b')
        self.assertEqual(get_max_occuring_char('abc'), 'a')
        self.assertEqual(get_max_occuring_char('aabbcc'), 'a')

    def test_edge_cases(self):
        self.assertEqual(get_max_occuring_char(''), '')
        self.assertEqual(get_max_occuring_char('a'), 'a')

    def test_boundary_cases(self):
        self.assertEqual(get_max_occuring_char('a' * 256), 'a')
        self.assertEqual(get_max_occuring_char('a' * 257), 'a')

    def test_corner_cases(self):
        self.assertEqual(get_max_occuring_char('abcabcabc'), 'a')
        self.assertEqual(get_max_occuring_char('abcdabcdabcd'), 'a')
        self.assertEqual(get_max_occuring_char('aabbccddeeff'), 'a')
