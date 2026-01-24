import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_first_repeated_char(self):
        self.assertEqual(first_Repeated_Char("abc"), 'a')
        self.assertEqual(first_Repeated_Char("aabbcc"), 'a')
        self.assertEqual(first_Repeated_Char("aabbccdd"), 'a')
        self.assertEqual(first_Repeated_Char("a"), 'a')
        self.assertEqual(first_Repeated_Char("abcde"), '\0')
        self.assertEqual(first_Repeated_Char(""), '\0')
        self.assertEqual(first_Repeated_Char("a"), 'a')
        self.assertEqual(first_Repeated_Char("ab"), 'a')
        self.assertEqual(first_Repeated_Char("abc"), 'a')
        self.assertEqual(first_Repeated_Char("abcd"), '\0')
        self.assertEqual(first_Repeated_Char("abcde"), '\0')
