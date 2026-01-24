import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(split_lowerstring("helloWorld"), ["hello", "world"])
        self.assertListEqual(split_lowerstring("PythonProgramming"), ["Python", "Programming"])

    def test_edge_input(self):
        self.assertListEqual(split_lowerstring(""), [])
        self.assertListEqual(split_lowerstring("a"), ["a"])
        self.assertListEqual(split_lowerstring("A"), [])
        self.assertListEqual(split_lowerstring("aA"), ["a", "A"])

    def test_complex_input(self):
        self.assertListEqual(split_lowerstring("1helloWorld2"), ["hello"])
        self.assertListEqual(split_lowerstring("helloWorld1"), ["hello", "World"])
        self.assertListEqual(split_lowerstring("helloWorld123"), ["hello", "World"])
        self.assertListEqual(split_lowerstring("helloWorld_123"), ["hello", "World"])
        self.assertListEqual(split_lowerstring("helloWorld123_"), ["hello", "World"])
