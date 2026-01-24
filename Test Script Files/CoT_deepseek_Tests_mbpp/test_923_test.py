import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(super_seq("", "", 0, 0), 0)

    def test_same_characters(self):
        self.assertEqual(super_seq("ABCD", "ABCD", 4, 4), 4)

    def test_different_characters(self):
        self.assertEqual(super_seq("ABC", "DEF", 3, 3), 3)

    def test_same_prefix(self):
        self.assertEqual(super_seq("ABC", "ABD", 3, 3), 3)

    def test_different_prefix(self):
        self.assertEqual(super_seq("ABC", "DEF", 3, 3), 3)

    def test_mismatched_lengths(self):
        self.assertEqual(super_seq("ABC", "DEFG", 3, 4), 3)

    def test_mismatched_characters(self):
        self.assertEqual(super_seq("ABC", "DEF", 3, 3), 3)

    def test_large_inputs(self):
        X = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Y = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.assertEqual(super_seq(X, Y, len(X), len(Y)), len(X))
