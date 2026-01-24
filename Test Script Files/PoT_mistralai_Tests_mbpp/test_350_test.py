import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(minimum_Length("abab"), 2)
        self.assertEqual(minimum_Length("aaa"), 1)
        self.assertEqual(minimum_Length("z"), 1)
        self.assertEqual(minimum_Length("aabbcc"), 1)

    def test_edge_case(self):
        self.assertEqual(minimum_Length(""), 0)
        self.assertEqual(minimum_Length("a"), 0)
        self.assertEqual(minimum_Length("aa"), 1)
        self.assertEqual(minimum_Length("aaaa"), 1)

    def test_corner_case(self):
        self.assertEqual(minimum_Length("zzzz"), 0)
        self.assertEqual(minimum_Length("zzzA"), 1)
        self.assertEqual(minimum_Length("ZZZ"), 0)
        self.assertEqual(minimum_Length("ZZZa"), 1)
