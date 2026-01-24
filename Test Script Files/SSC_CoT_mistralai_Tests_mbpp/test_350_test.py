import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(minimum_Length("algorithms"), 7)
        self.assertEqual(minimum_Length("programming"), 10)
        self.assertEqual(minimum_Length("python"), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(minimum_Length(""), 0)
        self.assertEqual(minimum_Length("a"), 1)
        self.assertEqual(minimum_Length("z"), 1)
        self.assertEqual(minimum_Length("aaa"), 3)
        self.assertEqual(minimum_Length("zzz"), 3)
        self.assertEqual(minimum_Length("aabbcc"), 3)
        self.assertEqual(minimum_Length("zzzzzz"), 6)

    def test_special_cases(self):
        self.assertEqual(minimum_Length("abab"), 3)
        self.assertEqual(minimum_Length("aabba"), 3)
        self.assertEqual(minimum_Length("abcd"), 4)
        self.assertEqual(minimum_Length("abcdefghijklmnopqrstuvwxyz"), 26)
        self.assertEqual(minimum_Length("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)
        self.assertEqual(minimum_Length("AbCdEfGhIjKlMnOpQrStUvWxYz"), 26)
