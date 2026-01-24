import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertIsInstance(array_3d(3, 4, 5), list)
        self.assertEqual(len(array_3d(3, 4, 5)), 5)
        self.assertEqual(len(array_3d(3, 4, 5)[0]), 4)
        self.assertEqual(len(array_3d(3, 4, 5)[0][0]), 3)
        self.assertEqual(array_3d(3, 4, 5)[2][1][2], '*')

    def test_edge_and_boundary_conditions(self):
        self.assertRaises(TypeError, array_3d, 'a', 4, 5)
        self.assertRaises(TypeError, array_3d, 3, 'a', 5)
        self.assertRaises(TypeError, array_3d, 3, 4, 'a')
        self.assertIsInstance(array_3d(0, 4, 5), list)
        self.assertIsInstance(array_3d(3, 0, 5), list)
        self.assertIsInstance(array_3d(3, 4, 0), list)
        self.assertEqual(len(array_3d(1, 1, 1)), 1)
        self.assertEqual(len(array_3d(1, 1, 2)[0]), 1)
        self.assertEqual(len(array_3d(1, 1, 2)[0][0]), 1)
        self.assertEqual(array_3d(1, 1, 1)[0][0][0], '*')
