import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_odd("abc"), "b")
        self.assertEqual(remove_odd("hello"), "llo")
        self.assertEqual(remove_odd("123"), "33")

    def test_empty(self):
        self.assertEqual(remove_odd(""), "")

    def test_single_char(self):
        self.assertEqual(remove_odd("a"), "a")
        self.assertEqual(remove_odd("b"), "")

    def test_edge(self):
        self.assertEqual(remove_odd("abcdef"), "bdf")
        self.assertEqual(remove_odd("123456"), "246")

    def test_long_string(self):
        self.assertEqual(remove_odd("abcdefghijklmnopqrstuvwxyz"), "bcdhjlnprstvwxz")
