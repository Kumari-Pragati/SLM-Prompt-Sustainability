import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split_upperstring("HelloWorld"), ["Hello", "World"])

    def test_edge_case1(self):
        self.assertEqual(split_upperstring("Hello"), ["Hello"])

    def test_edge_case2(self):
        self.assertEqual(split_upperstring("World"), ["World"])

    def test_edge_case3(self):
        self.assertEqual(split_upperstring(""), [])

    def test_edge_case4(self):
        self.assertEqual(split_upperstring("Hello"), ["Hello"])

    def test_edge_case5(self):
        self.assertEqual(split_upperstring("HelloWorld123"), ["Hello", "World"])

    def test_edge_case6(self):
        self.assertEqual(split_upperstring("HelloWorld123abc"), ["Hello", "World"])

    def test_edge_case7(self):
        self.assertEqual(split_upperstring("HelloWorld123abc456"), ["Hello", "World"])

    def test_edge_case8(self):
        self.assertEqual(split_upperstring("HelloWorld123abc456"), ["Hello", "World"])

    def test_edge_case9(self):
        self.assertEqual(split_upperstring("HelloWorld123abc456"), ["Hello", "World"])

    def test_edge_case10(self):
        self.assertEqual(split_upperstring("HelloWorld123abc456"), ["Hello", "World"])
