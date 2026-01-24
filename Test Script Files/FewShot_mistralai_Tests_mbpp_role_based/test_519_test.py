import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(volume_tetrahedron(1), 0.4794255386042031)
        self.assertAlmostEqual(volume_tetrahedron(2), 1.5533936063442464)
        self.assertAlmostEqual(volume_tetrahedron(3), 3.339741874848261)

    def test_zero(self):
        self.assertEqual(volume_tetrahedron(0), 0)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, volume_tetrahedron, -1)
        self.assertRaises(ValueError, volume_tetrahedron, -2)
