import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_Rotations("abc"), 1)
        self.assertEqual(find_Rotations("abcabc"), 1)
        self.assertEqual(find_Rotations("a"), 1)
        self.assertEqual(find_Rotations("abcabcabc"), 1)

    def test_edge(self):
        self.assertEqual(find_Rotations(""), 0)
        self.assertEqual(find_Rotations("a"), 1)
        self.assertEqual(find_Rotations("abcabc"), 1)

    def test_edge2(self):
        self.assertEqual(find_Rotations("a"), 1)
        self.assertEqual(find_Rotations("abcabc"), 1)
        self.assertEqual(find_Rotations("abcabcabc"), 1)

    def test_edge3(self):
        self.assertEqual(find_Rotations("a"), 1)
        self.assertEqual(find_Rotations("abcabc"), 1)
        self.assertEqual(find_Rotations("abcabcabc"), 1)

    def test_edge4(self):
        self.assertEqual(find_Rotations("a"), 1)
        self.assertEqual(find_Rotations("abcabc"), 1)
        self.assertEqual(find_Rotations("abcabcabc"), 1)

    def test_edge5(self):
        self.assertEqual(find_Rotations("a"), 1)
        self.assertEqual(find_Rotations("abcabc"), 1)
        self.assertEqual(find_Rotations("abcabcabc"), 1)
