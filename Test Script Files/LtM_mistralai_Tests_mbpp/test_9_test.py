import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):

    def test_simple_rotation(self):
        self.assertEqual(find_Rotations("abc"), 4)
        self.assertEqual(find_Rotations("abcd"), 4)
        self.assertEqual(find_Rotations("a"), 1)
        self.assertEqual(find_Rotations("aa"), 2)

    def test_edge_and_boundary(self):
        self.assertEqual(find_Rotations(""), 0)
        self.assertEqual(find_Rotations("abcdefghijklmnopqrstuvwxyz"), 26)
        self.assertEqual(find_Rotations("zabc"), 27)
        self.assertEqual(find_Rotations("az"), 53)

    def test_complex_scenarios(self):
        self.assertEqual(find_Rotations("abab"), 4)
        self.assertEqual(find_Rotations("ababcd"), 8)
        self.assertEqual(find_Rotations("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), 53)
