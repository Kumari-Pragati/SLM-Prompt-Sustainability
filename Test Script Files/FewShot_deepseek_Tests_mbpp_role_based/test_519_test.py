import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(volume_tetrahedron(1), 0.58, places=2)

    def test_boundary_condition(self):
        self.assertAlmostEqual(volume_tetrahedron(0), 0)

    def test_edge_condition(self):
        self.assertAlmostEqual(volume_tetrahedron(2), 4.16, places=2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            volume_tetrahedron('a')
