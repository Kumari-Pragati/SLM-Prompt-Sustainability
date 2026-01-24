import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(minimum_Length("a"), 1)
        self.assertEqual(minimum_Length("abc"), 2)
        self.assertEqual(minimum_Length("abcd"), 1)

    def test_edge(self):
        self.assertEqual(minimum_Length(""), 0)
        self.assertEqual(minimum_Length("a" * 26), 1)
        self.assertEqual(minimum_Length("a" * 26 + "b"), 2)

    def test_complex(self):
        self.assertEqual(minimum_Length("aabbcc"), 2)
        self.assertEqual(minimum_Length("aabbccdd"), 2)
        self.assertEqual(minimum_Length("aabbccddaa"), 2)
