import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):

    def test_volume_tetrahedron_positive_number(self):
        self.assertAlmostEqual(volume_tetrahedron(3), 10.39, places=2)

    def test_volume_tetrahedron_zero(self):
        self.assertEqual(volume_tetrahedron(0), 0)

    def test_volume_tetrahedron_negative_number(self):
        with self.assertRaises(ValueError):
            volume_tetrahedron(-3)
