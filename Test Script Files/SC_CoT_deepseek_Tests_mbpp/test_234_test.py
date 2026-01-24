import unittest

from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(volume_cube(3), 27)

    def test_edge_case(self):
        self.assertEqual(volume_cube(0), 0)
        self.assertEqual(volume_cube(1), 1)

    def test_boundary_case(self):
        self.assertEqual(volume_cube(10), 1000)
        self.assertEqual(volume_cube(100), 1000000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            volume_cube("a")
        with self.assertRaises(TypeError):
            volume_cube(None)
