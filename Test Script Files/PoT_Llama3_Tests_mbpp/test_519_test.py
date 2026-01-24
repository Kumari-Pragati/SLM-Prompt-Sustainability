import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(volume_tetrahedron(1), 0.47)

    def test_edge_case(self):
        self.assertEqual(volume_tetrahedron(0), 0.0)
        self.assertEqual(volume_tetrahedron(1e-6), 0.0)

    def test_edge_case_negative(self):
        self.assertEqual(volume_tetrahedron(-1), 0.0)
        self.assertEqual(volume_tetrahedron(-1e-6), 0.0)

    def test_edge_case_zero(self):
        self.assertEqual(volume_tetrahedron(0), 0.0)

    def test_edge_case_large(self):
        self.assertEqual(volume_tetrahedron(100), 0.47)

    def test_edge_case_large_negative(self):
        self.assertEqual(volume_tetrahedron(-100), 0.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            volume_tetrahedron('a')
