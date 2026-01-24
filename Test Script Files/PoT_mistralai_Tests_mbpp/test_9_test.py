import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_Rotations("abc"), 4)
        self.assertEqual(find_Rotations("a"), 1)
        self.assertEqual(find_Rotations("ab"), 2)
        self.assertEqual(find_Rotations("abcdef"), 6)
        self.assertEqual(find_Rotations("abcabc"), 3)

    def test_edge_cases(self):
        self.assertEqual(find_Rotations(""), 0)
        self.assertEqual(find_Rotations("a" * 1000), 1000)

    def test_corner_cases(self):
        self.assertEqual(find_Rotations("abab"), 4)
        self.assertEqual(find_Rotations("abcabcd"), 8)
        self.assertEqual(find_Rotations("abcabcabc"), 9)
