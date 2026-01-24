import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(max_char('aab'), 'a')
        self.assertEqual(max_char('abc'), 'a')

    def test_edge_conditions(self):
        self.assertEqual(max_char(''), '')
        self.assertEqual(max_char('a'), 'a')
        self.assertEqual(max_char('123'), '1')

    def test_complex_cases(self):
        self.assertEqual(max_char('aabbcc'), 'a')
        self.assertEqual(max_char('aabbccdd'), 'a')
        self.assertEqual(max_char('aabbccddeeff'), 'a')

    def test_special_characters(self):
        self.assertEqual(max_char('!@#$%^&*('), '!')

    def test_max_frequency(self):
        self.assertEqual(max_char('aabbbcc'), 'b')
        self.assertEqual(max_char('aabbbccdd'), 'b')
