import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(volume_cube(3), 27)

    def test_edge_cases(self):
        self.assertEqual(volume_cube(0), 0)
        self.assertEqual(volume_cube(1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(volume_cube(2.5), 15.625)

    def test_negative_input(self):
        self.assertRaises(ValueError, volume_cube, -1)

    def test_fractional_input(self):
        self.assertRaises(ValueError, volume_cube, 0.5)
