import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Rotations("abcde"), 1)

    def test_edge_case(self):
        self.assertEqual(find_Rotations("a"), 0)

    def test_boundary_case(self):
        self.assertEqual(find_Rotations(""), 0)

    def test_corner_case(self):
        self.assertEqual(find_Rotations("abcabcabc"), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Rotations(123)
