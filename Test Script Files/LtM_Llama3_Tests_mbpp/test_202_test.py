import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_even("abc"), "abc")
        self.assertEqual(remove_even("def"), "def")
        self.assertEqual(remove_even("ghi"), "ghi")

    def test_edge(self):
        self.assertEqual(remove_even(""), "")
        self.assertEqual(remove_even("a"), "a")
        self.assertEqual(remove_even("abc"), "abc")

    def test_edge2(self):
        self.assertEqual(remove_even("123456"), "135")
        self.assertEqual(remove_even("abcdef"), "ad")
        self.assertEqual(remove_even("abcdefg"), "adg")

    def test_edge3(self):
        self.assertEqual(remove_even("123456789"), "13579")
        self.assertEqual(remove_even("abcdefghijklmnopqrstuvwxyz"), "adghjklmnpqrstvwxz")
