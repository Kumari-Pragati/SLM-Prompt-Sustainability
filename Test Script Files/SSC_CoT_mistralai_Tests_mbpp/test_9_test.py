import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_Rotations("abcdefg"), 1)
        self.assertEqual(find_Rotations("123456"), 1)
        self.assertEqual(find_Rotations("ABCDEFG"), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Rotations(""), 0)
        self.assertEqual(find_Rotations("a"), 0)
        self.assertEqual(find_Rotations("abc"), 0)
        self.assertEqual(find_Rotations("abcdefg" * 2), 2)
        self.assertEqual(find_Rotations("abcdefg" * 3), 3)

    def test_rotated_strings(self):
        self.assertEqual(find_Rotations("abcdefg"), 1)
        self.assertEqual(find_Rotations("gdefcba"), 6)
        self.assertEqual(find_Rotations("12345678"), 8)
        self.assertEqual(find_Rotations("ABCDEFGHI"), 9)

    def test_invalid_input(self):
        self.assertRaises(TypeError, find_Rotations, 123)
        self.assertRaises(TypeError, find_Rotations, [])
        self.assertRaises(TypeError, find_Rotations, ())
        self.assertRaises(TypeError, find_Rotations, set())
        self.assertRaises(TypeError, find_Rotations, None)
