import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(upper_ctr("HelloWorld"), 2)
        self.assertEqual(upper_ctr("PythonProgramming"), 3)

    def test_edge_cases(self):
        self.assertEqual(upper_ctr(""), 0)
        self.assertEqual(upper_ctr("aBcDeF"), 2)

    def test_corner_cases(self):
        self.assertEqual(upper_ctr("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)
        self.assertEqual(upper_ctr("abcdefghijklmnopqrstuvwxyz"), 0)
        self.assertEqual(upper_ctr("1234567890!@#$%^&*()"), 0)
