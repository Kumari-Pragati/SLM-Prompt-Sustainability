import unittest
from mbpp_747_code import lcs_of_three

class TestLcsOfThree(unittest.TestCase):
    def test_typical_use_case(self):
        X = "ABC"
        Y = "ACD"
        Z = "ADE"
        m = len(X)
        n = len(Y)
        o = len(Z)
        result = lcs_of_three(X, Y, Z, m, n, o)
        self.assertEqual(result, 2)

    def test_edge_case_empty_strings(self):
        X = ""
        Y = ""
        Z = ""
        m = len(X)
        n = len(Y)
        o = len(Z)
        result = lcs_of_three(X, Y, Z, m, n, o)
        self.assertEqual(result, 0)

    def test_edge_case_single_character_strings(self):
        X = "A"
        Y = "B"
        Z = "C"
        m = len(X)
        n = len(Y)
        o = len(Z)
        result = lcs_of_three(X, Y, Z, m, n, o)
        self.assertEqual(result, 1)

    def test_edge_case_all_characters_match(self):
        X = "ABC"
        Y = "ABC"
        Z = "ABC"
        m = len(X)
        n = len(Y)
        o = len(Z)
        result = lcs_of_three(X, Y, Z, m, n, o)
        self.assertEqual(result, len(X))

    def test_edge_case_no_common_characters(self):
        X = "ABC"
        Y = "DEF"
        Z = "GHI"
        m = len(X)
        n = len(Y)
        o = len(Z)
        result = lcs_of_three(X, Y, Z, m, n, o)
        self.assertEqual(result, 0)
