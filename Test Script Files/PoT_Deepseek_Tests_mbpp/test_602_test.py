import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(first_repeated_char('abcab'), 'a')
        self.assertEqual(first_repeated_char('abcabc'), 'a')
        self.assertEqual(first_repeated_char('aabbcc'), 'None')

    def test_edge_cases(self):
        self.assertEqual(first_repeated_char(''), 'None')
        self.assertEqual(first_repeated_char('a'), 'None')

    def test_corner_cases(self):
        self.assertEqual(first_repeated_char('a'*10000 + 'b'), 'a')
        self.assertEqual(first_repeated_char('b'*10000 + 'a'), 'b')
