import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(first_Repeated_Char('abcabc'), 'a')
        self.assertEqual(first_Repeated_Char('abcd'), '\0')
        self.assertEqual(first_Repeated_Char('aabbcc'), 'a')

    def test_edge_cases(self):
        self.assertEqual(first_Repeated_Char(''), '\0')
        self.assertEqual(first_Repeated_Char('a'), '\0')
        self.assertEqual(first_Repeated_Char('aa'), 'a')

    def test_corner_cases(self):
        self.assertEqual(first_Repeated_Char('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), '\0')
        self.assertEqual(first_Repeated_Char('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZa'), 'a')
