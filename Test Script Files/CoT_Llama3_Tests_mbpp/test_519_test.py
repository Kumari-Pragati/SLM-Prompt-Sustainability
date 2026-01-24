import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(volume_tetrahedron(1), 0.97)

    def test_edge_case_zero(self):
        self.assertEqual(volume_tetrahedron(0), 0.0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            volume_tetrahedron(-1)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            volume_tetrahedron(1.5)

    def test_edge_case_non_numeric(self):
        with self.assertRaises(TypeError):
            volume_tetrahedron('a')

    def test_edge_case_large_input(self):
        self.assertEqual(volume_tetrahedron(100), 318.98)
