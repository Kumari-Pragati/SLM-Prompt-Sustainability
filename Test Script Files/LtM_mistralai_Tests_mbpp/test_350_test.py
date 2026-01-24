import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(minimum_Length("abc"), 3)
        self.assertEqual(minimum_Length("aaa"), 3)
        self.assertEqual(minimum_Length("zzz"), 3)

    def test_edge_input(self):
        self.assertEqual(minimum_Length(""), 0)
        self.assertEqual(minimum_Length("a"), 1)
        self.assertEqual(minimum_Length("aa"), 1)
        self.assertEqual(minimum_Length("zz"), 1)
        self.assertEqual(minimum_Length("aabbcc"), 2)

    def test_boundary_input(self):
        self.assertEqual(minimum_Length("z" * 26), 1)
        self.assertEqual(minimum_Length("a" * 26 + "z"), 26)
        self.assertEqual(minimum_Length("z" * 26 + "a"), 25)
