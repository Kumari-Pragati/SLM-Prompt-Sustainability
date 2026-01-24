import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(volume_tetrahedron(3), 0.24, places=2)

    def test_zero_input(self):
        with self.assertRaises(ZeroDivisionError):
            volume_tetrahedron(0)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            volume_tetrahedron(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            volume_tetrahedron(3.5)

    def test_edge_case(self):
        self.assertAlmostEqual(volume_tetrahedron(1), 0.04, places=2)
