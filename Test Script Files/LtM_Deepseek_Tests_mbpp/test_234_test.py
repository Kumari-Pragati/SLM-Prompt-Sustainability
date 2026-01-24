import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):

    def test_volume_cube_simple(self):
        self.assertEqual(volume_cube(2), 8)
        self.assertEqual(volume_cube(3), 27)

    def test_volume_cube_edge(self):
        self.assertEqual(volume_cube(0), 0)
        self.assertEqual(volume_cube(1), 1)

    def test_volume_cube_boundary(self):
        self.assertEqual(volume_cube(10), 1000)
        self.assertEqual(volume_cube(100), 1000000)

    def test_volume_cube_complex(self):
        self.assertEqual(volume_cube(2.5), 15.625)
        self.assertEqual(volume_cube(-2), -8)
