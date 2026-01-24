import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):

    def test_volume_tetrahedron_positive(self):
        self.assertAlmostEqual(volume_tetrahedron(1), 0.48, places=2)

    def test_volume_tetrahedron_negative(self):
        with self.assertRaises(TypeError):
            volume_tetrahedron(-1)

    def test_volume_tetrahedron_zero(self):
        self.assertAlmostEqual(volume_tetrahedron(0), 0.00, places=2)

    def test_volume_tetrahedron_non_numeric(self):
        with self.assertRaises(TypeError):
            volume_tetrahedron('a')
