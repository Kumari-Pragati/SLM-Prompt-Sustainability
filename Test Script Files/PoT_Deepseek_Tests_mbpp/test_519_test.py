import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(volume_tetrahedron(1), 0.58, places=2)

    def test_edge_case(self):
        self.assertAlmostEqual(volume_tetrahedron(0), 0)

    def test_boundary_case(self):
        self.assertAlmostEqual(volume_tetrahedron(2), 8.38, places=2)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            volume_tetrahedron(-1)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            volume_tetrahedron('a')
