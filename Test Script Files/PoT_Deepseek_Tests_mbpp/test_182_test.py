import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_character("HelloWorld123"), (['H', 'W'], ['e', 'o', 'l', 'l', 'o', 'r', 'd'], ['1', '2', '3'], []))
        self.assertEqual(find_character("aBcDeFgHiJkLmNoPqRsTuVwXyZ0123456789"), (['B', 'D', 'F', 'H', 'J', 'L', 'N', 'P', 'R', 'T', 'V', 'X', 'Z'], ['a', 'c', 'e', 'g', 'i', 'k', 'm', 'o', 'q', 's', 'u', 'w', 'y'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'], []))

    def test_edge_cases(self):
        self.assertEqual(find_character(""), ([], [], [], []))
        self.assertEqual(find_character(" "), ([], [], [], [',' ,' ']))

    def test_corner_cases(self):
        self.assertEqual(find_character("!@#$%^&*()"), ([], [], [], [',' ,'!' ,'@' ,'#' ,'$' ,'^' ,'&' ,'*' ,'(' ,')']))
