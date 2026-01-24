import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):
    def test_simple_string(self):
        self.assertEqual(lower_ctr("abc"), 3)
        self.assertEqual(lower_ctr("ABC"), 3)
        self.assertEqual(lower_ctr("abc123"), 3)
        self.assertEqual(lower_ctr("ABCdef"), 3)

    def test_edge_cases(self):
        self.assertEqual(lower_ctr(""), 0)
        self.assertEqual(lower_ctr("a"), 1)
        self.assertEqual(lower_ctr("z"), 1)
        self.assertEqual(lower_ctr("A"), 0)
        self.assertEqual(lower_ctr("Z"), 0)
        self.assertEqual(lower_ctr("0123456789"), 0)

    def test_complex_cases(self):
        self.assertEqual(lower_ctr("aBcDeFgHiJkLmNoPqRsTuVwXyZ"), 26)
        self.assertEqual(lower_ctr("aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTuVwXyZ"), 52)
        self.assertEqual(lower_ctr("!@#$%^&*()_+-=[]{};':\"|,.<>/?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789"), 0)
