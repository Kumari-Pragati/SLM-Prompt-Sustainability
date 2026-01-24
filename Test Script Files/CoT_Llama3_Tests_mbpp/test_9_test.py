import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(find_Rotations("hello"), 5)
        self.assertEqual(find_Rotations("world"), 5)
        self.assertEqual(find_Rotations("abcabc"), 3)

    def test_edge_cases(self):
        self.assertEqual(find_Rotations(""), 0)
        self.assertEqual(find_Rotations("a"), 1)
        self.assertEqual(find_Rotations("abc"), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Rotations(None)
        with self.assertRaises(TypeError):
            find_Rotations(123)

    def test_non_string_inputs(self):
        with self.assertRaises(TypeError):
            find_Rotations([1, 2, 3])
