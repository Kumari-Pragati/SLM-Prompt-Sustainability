import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):
    def test_simple_input(self):
        self.assertAlmostEqual(volume_tetrahedron(1), 0.4794255386042031)
        self.assertAlmostEqual(volume_tetrahedron(2), 2.479425538604203)
        self.assertAlmostEqual(volume_tetrahedron(3), 4.479425538604203)

    def test_edge_cases(self):
        self.assertAlmostEqual(volume_tetrahedron(0), 0)
        self.assertAlmostEqual(volume_tetrahedron(1e-5), 0)
        self.assertAlmostEqual(volume_tetrahedron(1e6), 40319.60784313775)
