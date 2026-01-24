import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_odd("abcdefg"), "acde")
        self.assertEqual(remove_odd(""), "")
        self.assertEqual(remove_odd("x"), "x")
        self.assertEqual(remove_odd("xx"), "x")

    def test_edge_case(self):
        self.assertEqual(remove_odd("a"), "a")
        self.assertEqual(remove_odd("aa"), "a")
        self.assertEqual(remove_odd("abc"), "ab")
        self.assertEqual(remove_odd("abcdef"), "abcd")
        self.assertEqual(remove_odd("abcdefg"), "acde")
        self.assertEqual(remove_odd("abcdefgh"), "abcdgh")
