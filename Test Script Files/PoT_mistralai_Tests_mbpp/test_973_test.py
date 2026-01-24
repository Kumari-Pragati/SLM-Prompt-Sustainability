import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(left_rotate("abc", 1), "bca")
        self.assertEqual(left_rotate("abc", 2), "cab")
        self.assertEqual(left_rotate("abc", 3), "cba")

    def test_edge_and_boundary_cases(self):
        self.assertEqual(left_rotate("", 2), "")
        self.assertEqual(left_rotate("a", 0), "a")
        self.assertEqual(left_rotate("aa", 1), "aa")
        self.assertEqual(left_rotate("abc", 0), "bc" )
        self.assertEqual(left_rotate("abc", 4), "abc")
