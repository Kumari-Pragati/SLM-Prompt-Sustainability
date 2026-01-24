import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):

    def test_simple_input(self):
        self.assertAlmostEqual(volume_tetrahedron(1), 0.58, 2)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(volume_tetrahedron(0), 0.0)
        self.assertAlmostEqual(volume_tetrahedron(math.sqrt(2)), 0.58, 2)

    def test_edge_cases(self):
        self.assertAlmostEqual(volume_tetrahedron(2), 2.31, 2)
        self.assertAlmostEqual(volume_tetrahedron(0.5), 0.14, 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            volume_tetrahedron("invalid")
        with self.assertRaises(ValueError):
            volume_tetrahedron(-1)
