import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(volume_tetrahedron(1), 0.4794255386042031)
        self.assertAlmostEqual(volume_tetrahedron(2), 2.356194490192345)
        self.assertAlmostEqual(volume_tetrahedron(3), 5.235987755982988)

    def test_edge_case(self):
        self.assertAlmostEqual(volume_tetrahedron(0), 0)
        self.assertAlmostEqual(volume_tetrahedron(1e-6), 0)
        self.assertAlmostEqual(volume_tetrahedron(1e6), 1000000)

    def test_corner_case(self):
        self.assertAlmostEqual(volume_tetrahedron(-1), -0.4794255386042031)
