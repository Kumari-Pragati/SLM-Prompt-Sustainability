import unittest
from mbpp_519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(volume_tetrahedron(1), 0.61)
        self.assertEqual(volume_tetrahedron(2), 1.22)
        self.assertEqual(volume_tetrahedron(3), 1.83)

    def test_edge_cases(self):
        self.assertEqual(volume_tetrahedron(0), 0.0)
        self.assertEqual(volume_tetrahedron(-1), 0.0)
        self.assertEqual(volume_tetrahedron(4), 2.44)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            volume_tetrahedron('a')
        with self.assertRaises(TypeError):
            volume_tetrahedron(None)
