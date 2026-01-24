import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(first_Repeated_Char("hello"), 'l')
        self.assertEqual(first_Repeated_Char("Python"), 't')
        self.assertEqual(first_Repeated_Char("Aardvark"), 'a')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(first_Repeated_Char(""), '\0')
        self.assertEqual(first_Repeated_Char("a"), 'a')
        self.assertEqual(first_Repeated_Char("aa"), 'a')
        self.assertEqual(first_Repeated_Char("ab"), '\0')
        self.assertEqual(first_Repeated_Char("abcdefghijklmnopqrstuvwxyz"), '\0')
        self.assertEqual(first_Repeated_Char("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), '\0')
        self.assertEqual(first_Repeated_Char("1234567890"), '\0')
        self.assertEqual(first_Repeated_Char("!@#$%^&*()_+-=[]{};:'\",.<>?/"), '\0')

    def test_special_and_corner_cases(self):
        self.assertEqual(first_Repeated_Char("aaa"), 'a')
        self.assertEqual(first_Repeated_Char("abab"), 'b')
        self.assertEqual(first_Repeated_Char("ababcdab"), 'a')
        self.assertEqual(first_Repeated_Char("ababcdabcdab"), 'a')
        self.assertEqual(first_Repeated_Char("ababcdabcdabcdab"), 'a')
        self.assertEqual(first_Repeated_Char("ababcdabcdabcdabcdab"), 'a')
