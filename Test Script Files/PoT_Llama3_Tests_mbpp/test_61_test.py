import unittest
from mbpp_61_code import count_Substrings

class TestCountSubstrings(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Substrings("123", 3), 2)

    def test_edge_case(self):
        self.assertEqual(count_Substrings("123", 1), 1)

    def test_edge_case2(self):
        self.assertEqual(count_Substrings("123", 4), 1)

    def test_edge_case3(self):
        self.assertEqual(count_Substrings("123", 0), 0)

    def test_edge_case4(self):
        self.assertEqual(count_Substrings("", 3), 0)

    def test_edge_case5(self):
        self.assertEqual(count_Substrings("123", -1), 0)

    def test_edge_case6(self):
        self.assertEqual(count_Substrings("123", 5), 1)

    def test_edge_case7(self):
        self.assertEqual(count_Substrings("123", 2), 1)

    def test_edge_case8(self):
        self.assertEqual(count_Substrings("123", 6), 0)

    def test_edge_case9(self):
        self.assertEqual(count_Substrings("123", 7), 0)

    def test_edge_case10(self):
        self.assertEqual(count_Substrings("123", 8), 0)
