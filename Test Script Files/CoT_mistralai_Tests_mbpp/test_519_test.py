import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):
    def test_positive_integer(self):
        self.assertAlmostEqual(volume_tetrahedron(1), 0.4794255386042031)
        self.assertAlmostEqual(volume_tetrahedron(2), 1.4307628685988963)
        self.assertAlmostEqual(volume_tetrahedron(3), 3.0479425538604204)

    def test_zero(self):
        self.assertEqual(volume_tetrahedron(0), 0.0)

    def test_negative_number(self):
        self.assertRaises(ValueError, volume_tetrahedron, -1)

    def test_fraction(self):
        self.assertRaises(ValueError, volume_tetrahedron, 0.5)

    def test_large_number(self):
        self.assertRaises(OverflowError, volume_tetrahedron, 1000000)
