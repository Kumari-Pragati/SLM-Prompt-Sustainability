import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):

    def test_lower_ctr(self):
        self.assertEqual(lower_ctr("Hello World"), 3)
        self.assertEqual(lower_ctr("abcdef"), 6)
        self.assertEqual(lower_ctr("123456"), 0)
        self.assertEqual(lower_ctr("abcdefghijklmnopqrstuvwxyz"), 26)
        self.assertEqual(lower_ctr("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 0)
        self.assertEqual(lower_ctr("aA1!"), 1)
        self.assertEqual(lower_ctr(""), 0)
