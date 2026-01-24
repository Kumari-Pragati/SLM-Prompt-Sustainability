import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(left_rotate("abc", 1), "bca")
        self.assertEqual(left_rotate("abc", 2), "cab")
        self.assertEqual(left_rotate("abc", 0), "abc")

    def test_edge_and_boundary(self):
        self.assertEqual(left_rotate("", 1), "")
        self.assertEqual(left_rotate("a", 1), "a")
        self.assertEqual(left_rotate("abc", 4), "cab")
        self.assertEqual(left_rotate("abc", len("abc")), "abc")

    def test_complex(self):
        self.assertEqual(left_rotate("abcdefg", 3), "cdefgab")
        self.assertEqual(left_rotate("abcdefg", 0), "cdefgab")
        self.assertEqual(left_rotate("abcdefg", len("abcdefg")), "abcdefg")
