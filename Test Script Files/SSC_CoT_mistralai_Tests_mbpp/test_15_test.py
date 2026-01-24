import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(split_lowerstring("HelloWorld"), ["hello", "world"])
        self.assertListEqual(split_lowerstring("PythonProgramming"), ["python", "programming"])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(split_lowerstring(""), [])
        self.assertListEqual(split_lowerstring("a"), ["a"])
        self.assertListEqual(split_lowerstring("ab"), ["a", "b"])
        self.assertListEqual(split_lowerstring("abcd"), ["abcd"])
        self.assertListEqual(split_lowerstring("aBcDeFgHiJkLmNoPqRsTuVwXyZ"), ["a", "B", "c", "D", "e", "F", "g", "h", "i", "j", "k", "L", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
        self.assertListEqual(split_lowerstring("12345"), [])
        self.assertListEqual(split_lowerstring("1A2B3C"), ["1", "A", "2", "B", "3", "C"])
        self.assertListEqual(split_lowerstring("A1B2C3"), ["A", "1", "B", "2", "C", "3"])
        self.assertListEqual(split_lowerstring("A1B2C3D"), ["A1B2C3D"])

    def test_special_cases(self):
        self.assertListEqual(split_lowerstring("HeLLoWorLd"), ["hello", "world"])
        self.assertListEqual(split_lowerstring("PyThOnPrOgRaMmInG"), ["python", "programming"])
        self.assertListEqual(split_lowerstring("ThIs iS a tEsT cAsE"), ["this", "is", "a", "test", "case"])
