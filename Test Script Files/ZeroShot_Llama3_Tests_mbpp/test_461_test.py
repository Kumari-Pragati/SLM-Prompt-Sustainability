import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):
    def test_upper_ctr(self):
        self.assertEqual(upper_ctr("Hello World"), 3)
        self.assertEqual(upper_ctr("hello world"), 0)
        self.assertEqual(upper_ctr("ABC123"), 3)
        self.assertEqual(upper_ctr("abc123"), 0)
        self.assertEqual(upper_ctr("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)
        self.assertEqual(upper_ctr("abcdefghijklmnopqrstuvwxyz"), 0)
        self.assertEqual(upper_ctr("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"), 26)
        self.assertEqual(upper_ctr("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)
        self.assertEqual(upper_ctr("1234567890"), 0)
        self.assertEqual(upper_ctr(" ABC DEF GHI"), 6)
        self.assertEqual(upper_ctr(" ABC DEF GHI JKL"), 6)
        self.assertEqual(upper_ctr(" ABC DEF GHI JKL MNO"), 6)
