import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(multiple_split("a;b,c*d\ne"), ["a", "b", "c", "*", "d", "\n", "e"])
        self.assertListEqual(multiple_split("a,b,c"), ["a", "b", "c"])
        self.assertListEqual(multiple_split("a*b\nc"), ["a", "*", "b", "\n", "c"])

    def test_edge_input(self):
        self.assertListEqual(multiple_split(""), [])
        self.assertListEqual(multiple_split(";"), [""])
        self.assertListEqual(multiple_split("a;"), ["a", ""])
        self.assertListEqual(multiple_split("a,*"), ["a", "*"])
        self.assertListEqual(multiple_split("a,*b"), ["a", "*", "b"])
        self.assertListEqual(multiple_split("a,*b,*"), ["a", "*", "b", "*"])

    def test_boundary_input(self):
        self.assertListEqual(multiple_split("a;b,c*d\ne "), ["a", "b", "c", "*", "d", "\n", "e"])
        self.assertListEqual(multiple_split("a,b,c,\n"), ["a", "b", "c", "\n"])
        self.assertListEqual(multiple_split("a*b\n c"), ["a", "*", "b", "\n", "c"])
        self.assertListEqual(multiple_split("a,*b\nc"), ["a", "*", "b", "\n", "c"])
