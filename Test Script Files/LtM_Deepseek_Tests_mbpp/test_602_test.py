import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(first_repeated_char('abcabc'), 'a')
        self.assertEqual(first_repeated_char('abcd'), 'None')

    def test_edge_conditions(self):
        self.assertEqual(first_repeated_char(''), 'None')
        self.assertEqual(first_repeated_char('a'), 'None')
        self.assertEqual(first_repeated_char('aa'), 'a')

    def test_complex_cases(self):
        self.assertEqual(first_repeated_char('aabbcc'), 'None')
        self.assertEqual(first_repeated_char('abcabcabc'), 'a')
        self.assertEqual(first_repeated_char('abcdabcd'), 'None')
        self.assertEqual(first_repeated_char('abcdabcdabcd'), 'a')
