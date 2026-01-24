import unittest
from mbpp_565_code import split

class TestSplitFunction(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(split("hello"), ["h", "e", "l", "l", "o"])

    def test_edge_cases(self):
        self.assertEqual(split(""), [])
        self.assertEqual(split("a"), ["a"])
        self.assertEqual(split("abcdefghijklmnopqrstuvwxyz"), ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])

    def test_boundary_cases(self):
        self.assertEqual(split("a "), ["a", " "])
        self.assertEqual(split("abcd\t"), ["a", "b", "c", "d"])
        self.assertEqual(split("abc\n"), ["a", "b", "c"])

    def test_special_cases(self):
        self.assertEqual(split("A1B2C3"), ["A", "1", "B", "2", "C", "3"])
        self.assertEqual(split("0123456789"), ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
