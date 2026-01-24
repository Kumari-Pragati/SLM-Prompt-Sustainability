import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):
    def test_typical_case(self):
        self.assertIsInstance(array_3d(3, 4, 5), list)
        self.assertEqual(len(array_3d(3, 4, 5)), 5)
        self.assertEqual(len(array_3d(3, 4, 5)[0]), 4)
        self.assertEqual(len(array_3d(3, 4, 5)[0][0]), 3)
        self.assertEqual(array_3d(3, 4, 5)[2][1][2], '*')

    def test_edge_case_small_dimensions(self):
        self.assertIsInstance(array_3d(1, 1, 1), list)
        self.assertEqual(len(array_3d(1, 1, 1)), 1)
        self.assertEqual(len(array_3d(1, 1, 1)[0]), 1)
        self.assertEqual(len(array_3d(1, 1, 1)[0][0]), 1)

    def test_edge_case_single_dimension(self):
        self.assertIsInstance(array_3d(1, 1, 0), list)
        self.assertEqual(len(array_3d(1, 1, 0)), 0)

    def test_edge_case_negative_dimensions(self):
        with self.assertRaises(ValueError):
            array_3d(-1, 1, 1)
        with self.assertRaises(ValueError):
            array_3d(1, -1, 1)
        with self.assertRaises(ValueError):
            array_3d(1, 1, -1)
