import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(volume_tetrahedron(1), 0.24, places=2)

    def test_edge_case_zero(self):
        with self.assertRaises(ZeroDivisionError):
            volume_tetrahedron(0)

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            volume_tetrahedron(-1)

    def test_edge_case_non_integer(self):
        self.assertAlmostEqual(volume_tetrahedron(1.5), 0.24, places=2)

    def test_edge_case_large(self):
        self.assertAlmostEqual(volume_tetrahedron(100), 12.0, places=2)
