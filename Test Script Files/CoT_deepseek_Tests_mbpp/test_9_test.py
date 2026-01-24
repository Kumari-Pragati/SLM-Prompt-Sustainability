import unittest
from mbpp_9_code import find_Rotations

class TestFindRotations(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Rotations('abcde'), 1)

    def test_edge_case(self):
        self.assertEqual(find_Rotations('a'), 0)

    def test_boundary_case(self):
        self.assertEqual(find_Rotations(''), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Rotations(123)

        with self.assertRaises(TypeError):
            find_Rotations(None)

        with self.assertRaises(TypeError):
            find_Rotations(123.45)

        with self.assertRaises(TypeError):
            find_Rotations(['a', 'b', 'c'])

        with self.assertRaises(TypeError):
            find_Rotations({'a': 1, 'b': 2, 'c': 3})

        with self.assertRaises(TypeError):
            find_Rotations(range(1, 4))

        with self.assertRaises(TypeError):
            find_Rotations(b'abc')
