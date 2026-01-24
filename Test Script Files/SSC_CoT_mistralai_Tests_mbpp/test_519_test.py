import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(volume_tetrahedron(3), 11.32074662680941)
        self.assertAlmostEqual(volume_tetrahedron(5), 125.0253154861103)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(volume_tetrahedron(0), 0.0)
        self.assertAlmostEqual(volume_tetrahedron(1), 2.8284271247461903)
        self.assertAlmostEqual(volume_tetrahedron(1000), 1663383.561944906)

    def test_negative_input(self):
        self.assertRaises(ValueError, volume_tetrahedron, -1)
