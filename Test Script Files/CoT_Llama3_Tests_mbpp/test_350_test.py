import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(minimum_Length("abc"), 1)
    def test_edge_case(self):
        self.assertEqual(minimum_Length("aabbcc"), 2)
    def test_edge_case2(self):
        self.assertEqual(minimum_Length("a"), 1)
    def test_edge_case3(self):
        self.assertEqual(minimum_Length("abcdefghijklmnopqrstuvwxyz"), 1)
    def test_edge_case4(self):
        self.assertEqual(minimum_Length("aabbccdd"), 2)
    def test_edge_case5(self):
        self.assertEqual(minimum_Length("aabbccddaa"), 2)
    def test_edge_case6(self):
        self.assertEqual(minimum_Length("a"), 1)
    def test_edge_case7(self):
        self.assertEqual(minimum_Length("abc"), 1)
    def test_edge_case8(self):
        self.assertEqual(minimum_Length("aabbcc"), 2)
    def test_edge_case9(self):
        self.assertEqual(minimum_Length("aabbccdd"), 2)
    def test_edge_case10(self):
        self.assertEqual(minimum_Length("aabbccddaa"), 2)
