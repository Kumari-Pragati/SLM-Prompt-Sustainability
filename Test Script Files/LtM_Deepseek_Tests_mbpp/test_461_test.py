import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):

    def test_upper_ctr_simple(self):
        self.assertEqual(upper_ctr("HelloWorld"), 2)
        self.assertEqual(upper_ctr("PythonProgramming"), 3)

    def test_upper_ctr_edge(self):
        self.assertEqual(upper_ctr(""), 0)
        self.assertEqual(upper_ctr("aBcDeF"), 2)

    def test_upper_ctr_boundary(self):
        self.assertEqual(upper_ctr("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)
        self.assertEqual(upper_ctr("abcdefghijklmnopqrstuvwxyz"), 0)
        self.assertEqual(upper_ctr("1234567890!@#$%^&*()"), 0)

    def test_upper_ctr_complex(self):
        self.assertEqual(upper_ctr("ABC123"), 3)
        self.assertEqual(upper_ctr("abc123"), 0)
        self.assertEqual(upper_ctr("AbC123"), 3)
