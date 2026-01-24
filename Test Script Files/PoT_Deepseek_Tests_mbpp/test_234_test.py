import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(volume_cube(1), 1)
        self.assertEqual(volume_cube(2), 8)
        self.assertEqual(volume_cube(3), 27)

    def test_edge_cases(self):
        self.assertEqual(volume_cube(0), 0)
        self.assertEqual(volume_cube(1.5), 3.375)

    def test_boundary_conditions(self):
        self.assertEqual(volume_cube(-1), -1)
        self.assertEqual(volume_cube(-2), -8)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            volume_cube('a')
        with self.assertRaises(TypeError):
            volume_cube(None)
        with self.assertRaises(TypeError):
            volume_cube([1, 2, 3])
