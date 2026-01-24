import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_parenthesis(["Hello (world)!"]), ["Hello world!"])

    def test_edge_case1(self):
        self.assertEqual(remove_parenthesis(["Hello (world)! (again)!"]), ["Hello world! again!"])

    def test_edge_case2(self):
        self.assertEqual(remove_parenthesis(["Hello (world)! (again)! (once more)!"]), ["Hello world! again! once more!"])

    def test_edge_case3(self):
        self.assertEqual(remove_parenthesis(["Hello (world)! (again)! (once more)! (and again)!"]), ["Hello world! again! once more! and again!"])

    def test_edge_case4(self):
        self.assertEqual(remove_parenthesis(["Hello (world)! (again)! (once more)! (and again)! (and once more)!"]), ["Hello world! again! once more! and again! and once more!"])

    def test_edge_case5(self):
        self.assertEqual(remove_parenthesis(["Hello (world)! (again)! (once more)! (and again)! (and once more)! (and again)!"]), ["Hello world! again! once more! and again! and once more! and again!"])

    def test_edge_case6(self):
        self.assertEqual(remove_parenthesis(["Hello (world)! (again)! (once more)! (and again)! (and once more)! (and again)! (and once more)!"]), ["Hello world! again! once more! and again! and once more! and again! and once more!"])

    def test_edge_case7(self):
        self.assertEqual(remove_parenthesis(["Hello (world)! (again)! (once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)!"]), ["Hello world! again! once more! and again! and once more! and again! and once more! and again!"])

    def test_edge_case8(self):
        self.assertEqual(remove_parenthesis(["Hello (world)! (again)! (once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)! (and once more)!"]), ["Hello world! again! once more! and again! and once more! and again! and once more! and again! and once more!"])

    def test_edge_case9(self):
        self.assertEqual(remove_parenthesis(["Hello (world)! (again)! (once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)!"]), ["Hello world! again! once more! and again! and once more! and again! and once more! and again! and once more! and again!"])

    def test_edge_case10(self):
        self.assertEqual(remove_parenthesis(["Hello (world)! (again)! (once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)! (and once more)!"]), ["Hello world! again! once more! and again! and once more! and again! and once more! and again! and once more! and again! and once more!"])

    def test_edge_case11(self):
        self.assertEqual(remove_parenthesis(["Hello (world)! (again)! (once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)!"]), ["Hello world! again! once more! and again! and once more! and again! and once more! and again! and once more! and again! and once more! and again!"])

    def test_edge_case12(self):
        self.assertEqual(remove_parenthesis(["Hello (world)! (again)! (once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)! (and once more)!"]), ["Hello world! again! once more! and again! and once more! and again! and once more! and again! and once more! and again! and once more! and again! and once more!"])

    def test_edge_case13(self):
        self.assertEqual(remove_parenthesis(["Hello (world)! (again)! (once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)! (and once more)! (and again)!"]), ["Hello world! again! once more! and again! and once